import pygame

class Brick():
    """
    Destroyable stuff
    """
    def __init__(self, x, y, block_size, img):
        self.x = x
        self.y = y
        self.width = 3*block_size
        self.height = 2*block_size
        self.rect = (self.x, self.y, self.width, self.height)
        self.hitbox = pygame.Rect(self.rect)
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))

        
        