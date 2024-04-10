import pygame

class Score():
    """
    Manage the score dixplay and increment
    """    
    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.digit_width = 2*block_size
        self.digit_height = 3*block_size
        self.digit_nb = 5
        self.digit_img = [pygame.image.load(f'assets/{i}.png') for i in range(10)]
        self.digit_img = [pygame.transform.scale(img, (self.digit_width, self.digit_height)) for img in self.digit_img]
        self.value = 0
    
    def draw(self, window):
        images = self.get_scores_img()
        for i in range(len(images)):
            window.blit(images[i], (self.x+i*self.digit_width,self.y))
            
    def get_scores_img(self):
        str_score = str(self.value).zfill(5)
        return [self.digit_img[int(char)] for char in str_score]