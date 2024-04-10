import pygame

class Paddle():
    """
    Player controlled paddle
    """
    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.width = 4*block_size
        self.height = 2*block_size
        self.vel = 5
        self.rect = (self.x, self.y, self.width, self.height)
        self.hitbox = pygame.Rect(self.rect)
        self.collide_countdown = 5
        
    def draw(self, window):
        pygame.draw.rect(window,'darkturquoise', self.rect)
        
    def move(self, direction):
        self.x += direction*self.vel
        self.rect = (self.x, self.y, self.width, self.height)
        self.hitbox = pygame.Rect(self.rect)
        
        