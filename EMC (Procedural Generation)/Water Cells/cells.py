import pygame


class Tile():
    
    def __init__(self, **kwargs) -> None:
        self.x = kwargs.get('x', 0)
        self.y = kwargs.get('y', 0)
        self.width = kwargs.get('width', 10)
        self.height = kwargs.get('height', 10)
        self.color = kwargs.get('color', (0, 0, 0))
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
    
    def rule(self):
        pass

class Grid():
    
    def __init__(self, **kwargs) -> None:
        self.screen = kwargs.get('screen', None)
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.cell_width = kwargs.get('cell_width', 10)
        self.rows = kwargs.get('rows', self.width//self.cell_width)
        self.cols = kwargs.get('cols', self.height//self.cell_width)
        default_tile = kwargs.get('default_tile', Tile)
        self.grid = [[default_tile for j in range(self.cols)] for _ in range(self.rows)]x    
    
    def draw(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.grid[x][y].draw(self.screen)