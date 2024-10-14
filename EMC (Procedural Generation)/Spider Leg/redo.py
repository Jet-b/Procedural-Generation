import pygame
import math


class Leg():
    
    def __init__(self, screen, **kwargs) -> None:
        self.segments = kwargs.get('segments', 1)
        self.lengths = kwargs.get('lengths', [100 for _ in range(self.segments)])
        self.lengths = [0] + self.lengths
        self.screen = screen
        self.origin = kwargs.get('origin', (self.screen.get_width()//2, self.screen.get_height()//2))
        self.positions = [(self.origin[0] + i, self.origin[1]) for i in self.lengths]
        self.angles = [0 for _ in range(self.segments)]
        self.max_length = sum(self.lengths)
        self.widths = kwargs.get('widths', [self.segments + 1 - i for i in range(self.segments)])
        self.angle = None
    
    # find the angle of the line between two points from horizontal
    def find_angle(self, target, origin):
        if origin == None:
            origin = self.origin
        dx = target[0] - self.origin[0]
        dy = target[1] - self.origin[1]
        angle = math.atan2(dy, dx)
        return angle
    
    # set the angle between the orign and the target
    def set_angle(self, pos):
        self.angle = self.find_angle(pos, self.origin)
    
    # draw a line with length and angle and starting position origin
    def draw_line(self, origin, length, angle, width=2):
        pygame.draw.line(self.screen, (255, 255, 255), origin, (origin[0] + length * math.cos(angle), origin[1] + length * math.sin(angle)), width)
    
    def find_D(self, x, y):
        D = (x**2 + y**2)**0.5
        self.D = D
        return D

def main():
    pygame.init()

    WIDTH, HEIGHT = 800, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    
    leg = Leg(screen, segments=3, lengths=[100, 100, 100])
    while True:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
        
        
        screen.fill((0, 0, 0))
        
        
        leg.draw()
        
        
        
        
        pygame.display.flip()

if __name__ == '__main__':
    main()