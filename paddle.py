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
        self.img = pygame.image.load('assets/paddle.png')
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
        
    def move(self, direction):
        self.x += direction*self.vel
        self.rect = (self.x, self.y, self.width, self.height)
        self.hitbox = pygame.Rect(self.rect)
        
        