import pygame 
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class SpiderLeg():
    
    def __init__(self, screen, **kwargs) -> None:
        self.screen = screen
        self.segments = kwargs.get('segments', 1)
        self.lengths = kwargs.get('lengths', [100 for _ in range(self.segments)])
        self.lengths = [0] + self.lengths
        self.positions = kwargs.get('positions', [(self.screen.get_width()//2 + i, self.screen.get_height()//2) for i in self.lengths])
        self.lengths = self.lengths[1:]
        self.angles = kwargs.get('angles', [0 for _ in range(self.segments)])
        self.widths = kwargs.get('widths', [2 for _ in range(self.segments)])
        self.distance = sum(self.lengths)
        if self.segments != len(self.lengths) != len(self.angles) != len(self.widths) != len(self.positions):
            raise ValueError('Lengths of lengths, angles, widths and positions must be equal to segments')
    
    
    def point(self, x, y):
        angles = []
        for i in range(self.segments):
            angles.append(math.atan2(y - self.positions[i][1],x - self.positions[i][0]))
        self.angles = angles
    
    def draw(self):
        for i in range(self.segments):
            pygame.draw.line(self.screen, (255, 255, 255), self.positions[i], (self.positions[i][0] + self.lengths[i] * math.cos(self.angles[i]), self.positions[i][1] + self.lengths[i] * math.sin(self.angles[i])), self.widths[i])


leg = SpiderLeg(screen, segments=3)
screen.fill((0, 0, 0))
while True:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            leg.point(x, y)
    
    
    leg.draw()
    
    pygame.display.flip()