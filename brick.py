import pygame

class Brick():
    """
    Destroyable stuff
    """
    def __init__(self, x, y, block_size, color):
        self.x = x
        self.y = y
        self.width = 3*block_size
        self.height = 2*block_size
        self.rect = (self.x, self.y, self.width, self.height)
        self.hitbox = pygame.Rect(self.rect)
        self.color = color
        
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

        
        