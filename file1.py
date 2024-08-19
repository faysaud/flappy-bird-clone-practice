# Flappy Bird clone
import pygame 
import sys 
from file2 import Game


pygame.init()
screen = pygame.display.set_mode((400, 650))
clock = pygame.time.Clock()
# Pygame is continually monitoring game events (key presses, mouse clicks, etc.). Iterate through the list of events and check to see if the user is quitting Pygame (clicking the X icon) and then stop the game.
game = Game('img_source/bluebird.png', 'img_source/pipe-green.png', 'img_source/background-day.png', 'img_source/base.png')
game.resize_images()

# create a new event 
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 800) #set_timer(event:int|Event, millis: int)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_SPACE and game.active:
                game.flap()
            if event.key == pygame.K_SPACE and game.active == False:
             game.restart()       
        if event.type == SPAWNPIPE:   
            game.add_pipe() 
      

    game.show_background(screen)
    game.show_ground(screen)       

    if game.active:
        game.show_bird(screen)
        game.update_bird()
        game.move_pipes()
        game.show_pipes(screen)
        game.check_collision()
        game.update_score()
        game.show_score('playing', screen, (255, 255, 255))
        game.update_high_score()
    else: 
        if game.lifes < 2:
            game.game_over(screen,(255, 255, 255))
        else:    
            game.end_of_life_screen(screen)

        

    pygame.display.update()
    clock.tick(120)    