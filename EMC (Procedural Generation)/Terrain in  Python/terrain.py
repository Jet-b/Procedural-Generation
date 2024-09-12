import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 1920, 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

BEIGE = (245, 245, 220)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(t, a1, a2):
    return a1 + t * (a2 - a1)

def grad(hash, x, y):
    h = hash & 3
    u = x if h & 1 == 0 else -x
    v = y if h & 2 == 0 else -y
    return u + v

def generate_permutation_table(seed=None):
    # Generate and shuffle the permutation table
    p = list(range(256))
    if seed is not None:
        random.seed(seed)
    random.shuffle(p)
    return p * 2  # Duplicate it for wraparound

def perlin(x, y, p):
    # Determine grid cell coordinates
    X = math.floor(x) & 255
    Y = math.floor(y) & 255
    
    # Relative x, y of point in cell
    x -= math.floor(x)
    y -= math.floor(y)
    
    # Fade curves for x, y
    u = fade(x)
    v = fade(y)
    
    # Hash coordinates of the 4 square corners
    A = p[X] + Y
    AA = p[A]
    AB = p[A + 1]
    B = p[X + 1] + Y
    BA = p[B]
    BB = p[B + 1]
    
    # Add blended results from all 4 corners
    return lerp(v, lerp(u, grad(p[AA], x, y),
                        grad(p[BA], x - 1, y)),
                   lerp(u, grad(p[AB], x, y - 1),
                        grad(p[BB], x - 1, y - 1)))

class Terrain():
    
    def __init__(self, **kwargs) -> None:
        self.screen = kwargs.get('screen', None)
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.cell_width = kwargs.get('cell_width', 1)
        self.rows = kwargs.get('rows', self.width//self.cell_width)
        self.cols = kwargs.get('cols', self.height//self.cell_width)
        self.grid = [[None for j in range(self.cols)] for _ in range(self.rows)]
        self.colour_map = kwargs.get("colour_map", {
            "G": (171,197,118),
            "F": (151,174,76),
            "M": (134,150,126),
            "S": (243, 245, 240)
            })
        self.permutation_table = generate_permutation_table(kwargs.get('seed', None))
    
    def draw(self):
        for x in range(self.rows):
            for y in range(self.cols):
                colour = self.cell_to_colour(x,y)
                pygame.draw.rect(self.screen, colour, (x*self.cell_width, y*self.cell_width, self.cell_width, self.cell_width), 0)
    
    def get_cell(self, x, y):
        return self.grid[x][y]
    
    def cell_to_colour(self, x, y):
        cell_type = self.get_cell(x, y)
        for cell in self.colour_map.keys():
            if cell_type == cell:
                return self.colour_map[cell]
        return self.grid[x][y]
    
    def reset(self):
        self.grid = [[None for j in range(self.cols)] for _ in range(self.rows)]
    
    def add_perlin_noise(self, scale=0.01):
        self.permutation_table = generate_permutation_table()
        for i in range(self.rows):
            for j in range(self.cols):
                # Generate Perlin noise for the grid cell
                noise_value = perlin(i * scale, j * scale, self.permutation_table)
                
                # Map the noise value to a colour
                noise_value += 1
                self.grid[i][j] = (noise_value*(255/2), noise_value*(255/2), noise_value*(255/2))
                
                # Map the noise value to different terrain types
                # if noise_value < -0.2:
                #     self.grid[i][j] = 'G'  # Mountain
                # elif noise_value < 0:
                #     self.grid[i][j] = 'F'  # Forest
                # elif noise_value < 0.2:
                #     self.grid[i][j] = 'M'  # Grass
                # else:
                #     self.grid[i][j] = 'S'  # Snow
    
    def debug_draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                pygame.draw.rect(self.screen, RED, (i*self.cell_width, j*self.cell_width, self.cell_width, self.cell_width), 1)

terrain = Terrain(screen=screen)
terrain.add_perlin_noise()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Resetting terrain")
                terrain.reset()
                terrain.add_perlin_noise()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            # if event.key == pygame.K_s:
            #     terrain.cell_width -= 1
            # if event.key == pygame.K_w:
            #     terrain.cell_width += 1
    
    screen.fill(WHITE)
    
    terrain.debug_draw()
    terrain.draw()
    
    pygame.display.flip()