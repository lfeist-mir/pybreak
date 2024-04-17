from paddle import Paddle
from ui import UI
from brick import Brick
from ball import Ball
from score import Score
import pygame

ENEMY_IMGS = ['assets/red_enemy.png','assets/orange_enemy.png','assets/yellow_enemy.png','assets/green_enemy.png','assets/turquoise_enemy.png','assets/blue_enemy.png','assets/purple_enemy.png']
ENEMY_LINES = 8
ENEMY_PER_LINE = 8

class GameManager():
    
    def __init__(self, width, height):
        self.block_size = int(width/50)
        self.ui = UI(width,height,self.block_size)
        self.paddle_init_pos = (13*self.block_size, 33*self.block_size)
        self.paddle = Paddle(
            self.paddle_init_pos[0], 
            self.paddle_init_pos[1], 
            self.block_size)
        self.clock = pygame.time.Clock()
        self.enemies = []
        for i in range(ENEMY_LINES):
            for j in range(ENEMY_PER_LINE):
                self.enemies.append(Brick(3*self.block_size+(i*3)*self.block_size,
                                          5*self.block_size+(j*2)*self.block_size,
                                          block_size=self.block_size,
                                          img=ENEMY_IMGS[(i*8+j)%len(ENEMY_IMGS)]
                                          ))
        self
        self.ball_init_pos = (self.paddle.x+round(self.paddle.width/2),
                              self.paddle.y-(self.block_size/2))
        self.ball = Ball(self.ball_init_pos[0],
                         self.ball_init_pos[1],
                         self.block_size)
        self.score = Score(33*self.block_size, 11*self.block_size, self.block_size)
        self.paddle_sound = pygame.mixer.Sound('assets/impact_paddle.wav')
        self.paddle_sound.set_volume(0.4)
        self.wall_sound = pygame.mixer.Sound('assets/impact_wall.wav')
        self.wall_sound.set_volume(0.4)
        self.brick_sound = pygame.mixer.Sound('assets/impact_brick.wav')
        self.brick_sound.set_volume(0.4)
        self.lives = 3
        
    def draw_main_loop(self):
        self.clock.tick(60)
        self.ui.draw_background()
        self.paddle.draw(self.ui.window)
        for enemy in self.enemies:
            enemy.draw(self.ui.window)
        self.ball.draw(self.ui.window)
        self.score.draw(self.ui.window)
        #draw lives
        for i in range(self.lives):
            self.ui.window.blit(self.paddle.img, ((31+5*i)*self.block_size,
                                                  22*self.block_size))
        pygame.display.flip()
        
    def handle_ball_wall_colision(self):
        '''
        Handle ball movbement if collision with a wall
        '''
        ball_left_x = self.ball.x-self.ball.radius
        ball_right_x = self.ball.x+self.ball.radius
        ball_upper_y = self.ball.y-self.ball.radius
        ball_lower_y = self.ball.y+self.ball.radius
        # Check lateral collision
        if ball_left_x <= self.ui.left_wall_x or ball_right_x >= self.ui.right_wall_x:
            # lateral collision
            self.ball.hor_direction *= -1
            self.wall_sound.play()
            self.ball.collisions += 1
        
        if ball_upper_y <= self.ui.upper_wall_y or ball_lower_y >= self.ui.lower_wall_y:
            self.ball.vert_direction *= -1
            self.wall_sound.play()
            self.ball.collisions += 1
    
    def handle_ball_paddle_colision(self):
        '''
        Handle ball movement if collision with the paddle
        '''
        # lower ball / up paddle collision
        ball_within_paddle_width = (self.paddle.hitbox.left-self.ball.radius <= self.ball.x <= self.paddle.hitbox.right+self.ball.radius)
        ball_within_paddle_height = (self.paddle.hitbox.top-self.ball.radius <= self.ball.y <= self.paddle.hitbox.bottom+self.ball.radius)
        
        if self.vertical_collision_happened(self.ball, self.paddle) and ball_within_paddle_width:
            self.ball.vert_direction *= -1
            self.paddle_sound.play()
            self.ball.collisions += 1
            
            
        if self.lateral_collision_happened(self.ball, self.paddle) and ball_within_paddle_height and self.paddle.collide_countdown == 0:
            self.ball.hor_direction *= -1
            self.paddle.collide_countdown = 10
            self.paddle_sound.play()         
            self.ball.collisions += 1  
            
        
    
    def handle_ball_enemy_colision(self):
        '''
        Handle ball movement if collision with the enemy
        '''
        for enemy in self.enemies:
            destroy_brick = False
            ball_within_enemy_width = (enemy.hitbox.left <= self.ball.x <= enemy.hitbox.right)
            ball_within_enemy_height = (enemy.hitbox.top <= self.ball.y <= enemy.hitbox.bottom+5)
            
            if self.vertical_collision_happened(self.ball, enemy) and ball_within_enemy_width:
                self.ball.vert_direction *= -1
                destroy_brick = True

                
            if self.lateral_collision_happened(self.ball, enemy) and ball_within_enemy_height:
                self.ball.hor_direction *= -1
                destroy_brick = True
            
            if destroy_brick:
                self.enemies.remove(enemy)
                self.score.value += 5
                self.brick_sound.play()
                self.ball.collisions += 1
                break
                
                
    def lateral_collision_happened(self,object_1, object_2):
        if (abs(object_1.hitbox.left - object_2.hitbox.right) <= 2) or (abs(object_2.hitbox.left - object_1.hitbox.right) <= 2):
            return True
        return False
    
    def vertical_collision_happened(self,object_1, object_2):
        return abs(object_1.hitbox.top - object_2.hitbox.bottom) <=2 or               abs(object_2.hitbox.top - object_1.hitbox.bottom) <=2
    
    
    def is_ball_alive(self):
        if self.ball.y > 36*self.block_size:
            #lose a live and reset
            self.lives -= 1
            self.paddle.x = self.paddle_init_pos[0]
            self.paddle.y = self.paddle_init_pos[1]
            self.ball.x = self.ball_init_pos[0]
            self.ball.y = self.ball_init_pos[1]
            self.ball.is_moving = False
            self.ball.vel = self.ball.init_vel
            self.ball.hor_direction = 1
            self.ball.vert_direction = -1
            self.ball.collisions = 0
            self.ui.set_img('assets/bg_start.png')

            