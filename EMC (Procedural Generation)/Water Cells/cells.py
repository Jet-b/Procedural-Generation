import pygame


class Grid():
    
    def __init__(self, screen, cellWidth):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.grid = set()
        self.cellWidth = cellWidth
    
    def fillAll(self, cell):
        for i in range(0, self.width, self.cellWidth):
            for j in range(0, self.height, self.cellWidth):
                c = cell(i, j, self.cellWidth)
                self.grid.add(c)
    
    def display(self):
        for cell in self.grid:
            cell.draw(self.screen)
    
    def getCellCollision(self, x, y):
        for cell in self.grid:
            if cell.collidepoint(x, y):
                return cell
        return None

    def getCell(self, x, y):
        for cell in self.grid:
            if cell.rect.x == x and cell.rect.y == y:
                return cell
        return None

    def fillUpTo(self, y, cell):
        for i in range(0, self.width, self.cellWidth):
            for j in range(0, y, self.cellWidth):
                self.grid.remove(self.getCell(i, j))
                c = cell(i, j, self.cellWidth)
                self.grid.add(c)

class Cell():
    
    def __init__(self, x, y, width, color):
        self.rect = pygame.Rect(x, y, width, width)
        self.color = color
    
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class WaterCell(Cell):
    
    def __init__(self, x, y, width):
        super().__init__(x, y, width, (116,204,244))
    
    def update(self):
        pass
    
    def __str__(self):
        return f'WaterCell({self.rect.x}, {self.rect.y}, {self.rect.width}, {self.rect.height})'

class AirCell(Cell):
        
        def __init__(self, x, y, width):
            super().__init__(x, y, width, (255,255,255))
        
        def update(self):
            pass
        
        def __str__(self):
            return f'AirCell({self.rect.x}, {self.rect.y}, {self.rect.width}, {self.rect.height})'

class GridHandler():
    
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.CELLWIDTH = 10
        self.grid = Grid(self.screen, self.CELLWIDTH)
        
        self.grid.fillAll(WaterCell)
        self.grid.fillUpTo(300, AirCell)
        
        self.running = True

    def run(self):
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill((0, 0, 0))
            self.grid.display()
            pygame.display.flip()
            
            pygame.time.Clock().tick(60)
        
        pygame.quit()


if __name__ == '__main__':
    pygame.init()
    GridHandler().run()