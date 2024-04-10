import pygame

class Ball():
    
    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.radius = int(block_size/2)
        self.color = 'white'
        self.vel = 4
        self.is_moving = False
        self.hor_direction=1
        self.vert_direction=1
        self.rect = (self.x-self.radius, self.y-self.radius, 2*self.radius, 2*self.radius)
        self.hitbox = pygame.Rect(self.rect)
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
        
    def move(self):
        self.x += self.hor_direction*self.vel
        self.y += self.vert_direction*self.vel
        self.rect = (self.x-self.radius, self.y-self.radius, 2*self.radius, 2*self.radius)
        self.hitbox = pygame.Rect(self.rect)