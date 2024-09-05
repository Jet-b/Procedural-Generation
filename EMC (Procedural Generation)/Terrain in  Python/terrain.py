import pygame

pygame.init()

WIDTH, HEIGHT = 800, 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))

BEIGE = (245, 245, 220)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Terrain():
    
    def __init__(self, **kwargs) -> None:
        self.screen = kwargs.get('screen', None)
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.cell_width = kwargs.get('cell_width', 10)
        self.rows = kwargs.get('rows', self.width//self.cell_width)
        self.cols = kwargs.get('cols', self.height//self.cell_width)
        self.grid = [[None for j in range(self.cols)] for _ in range(self.rows)]
    
    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                pass

class Tile():
    
    def __init__(self) -> None:
        pass

terrain = Terrain(screen=screen)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill(WHITE)
    
    terrain.draw()
    
    pygame.display.flip()