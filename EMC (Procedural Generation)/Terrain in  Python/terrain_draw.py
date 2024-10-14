import pygame

DEFAULT_WIDTH = 10
DEFAULT_MAP = {
            0: (171,197,118),
            1: (151,174,76),
            2: (134,150,126),
            3: (243, 245, 240)
            }

class Tile():
    
    def __init__(self, **kwargs) -> None:
        self.screen = kwargs.get('screen', None)
        self.x = kwargs.get('x', 0)
        self.y = kwargs.get('y', 0)
        self.width = kwargs.get('width', DEFAULT_WIDTH)
        self.val = kwargs.get('val', 0)
        self.number_map = kwargs.get("number_map", DEFAULT_MAP)
    
    def draw_cell(self):
        try:
            pygame.draw.rect(self.screen, self.number_map[self.val], (self.x, self.y, self.width, self.width), 0)
            return True
        except:
            print(f"Error drawing tile at x: {self.x}, y: {self.y}")
            return False
    
    def check_collision(self, x, y):
        if self.x < x < self.x + self.width and self.y < y < self.y + self.width:
            return True
        return False
    
    def set_val(self, val):
        self.val = val
    
    def increment_val(self):
        self.val = min(self.val + 1, max(self.number_map.keys()))
    
    def decrement_val(self):
        self.val = max(self.val - 1, min(self.number_map.keys()))

class TerrainMap():
    
    def __init__(self, **kwargs) -> None:
        self.screen = kwargs.get('screen', None)
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.cell_width = kwargs.get('cell_width', DEFAULT_WIDTH)
        self.rows = kwargs.get('rows', self.screen_width//self.cell_width)
        self.cols = kwargs.get('cols', self.screen_height//self.cell_width)
        self.number_map = kwargs.get("number_map", DEFAULT_MAP)
        self.grid = [
                    [
                    Tile(screen = self.screen, x = j, y = i, width = self.cell_width, val = 0, number_map = self.number_map)
                    for i in range(0, self.screen_height, self.cell_width)
                    ]
                    for j in range(0, self.screen_width, self.cell_width)
                    ]
    
    
    def increment_tile(self, x, y):
        self.grid[x//self.cell_width][y//self.cell_width].increment_val()
    
    def decrement_tile(self, x, y):
        self.grid[x//self.cell_width][y//self.cell_width].decrement_val()
    
    def increment_circle(self, x, y, radius):
        x = x//self.cell_width
        y = y//self.cell_width
        for i in range(x - radius, x + radius):
            for j in range(y - radius, y + radius):
                if 0 <= i < self.rows and 0 <= j < self.cols:
                    self.grid[i][j].increment_val()
    
    def draw_cells(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.grid[x][y].draw_cell()


class Main():
    
    def __init__(self) -> None:
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.terrain_map = TerrainMap(screen = self.screen, cell_width = 10)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    if event.buttons[0]:
                        self.terrain_map.increment_circle(x, y, 5)
                    if event.buttons[2]:
                        self.terrain_map.decrement_tile(x, y)

            self.screen.fill((0, 0, 0))
            self.terrain_map.draw_cells()
            pygame.display.flip()
        
            

if __name__ == "__main__":
    Main()