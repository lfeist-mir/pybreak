import pygame
from paddle import Paddle

class UI():
    '''
    This class manage the UI:
    - draw
    - events
    - ...
    '''
    def __init__(self, width, height, block_size):
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pybreak")
        self.block_size = block_size      
        self.left_wall_x = 3*self.block_size+1
        self.right_wall_x = 27*self.block_size
        self.upper_wall_y = 3*self.block_size+1
        self.lower_wall_y = 37*self.block_size
        self.img = pygame.image.load('assets/bg.png')
        self.img = pygame.transform.scale(self.img, (width, height))


    def draw_background(self):
        self.window.blit(self.img, (0,0))   

        