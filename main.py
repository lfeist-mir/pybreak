import pygame
from game_manager import GameManager

LEFT = -1
RIGHT = 1

pygame.init()
pygame.mixer.init()

#gm = GameManager(800,640)
gm = GameManager(1200,960)
pygame.mixer.music.load("assets/stage_01.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.8)


run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    gm.draw_main_loop()
    
    if gm.ball.is_moving:
        
        if gm.paddle.collide_countdown > 0:
            gm.paddle.collide_countdown -= 1
        gm.handle_ball_wall_colision()
        gm.handle_ball_paddle_colision()
        gm.handle_ball_enemy_colision()
        gm.ball.move()
    
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_LEFT] and gm.paddle.x > gm.ui.left_wall_x:
        gm.paddle.move(LEFT)
        
    if keys[pygame.K_RIGHT] and gm.paddle.x+gm.paddle.width < gm.ui.right_wall_x:
        gm.paddle.move(RIGHT)
        
    if keys[pygame.K_SPACE] and not gm.ball.is_moving:
        gm.ball.is_moving = True
        
    
    
pygame.mixer.music.stop()
pygame.quit()