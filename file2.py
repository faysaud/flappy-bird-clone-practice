# File for Game class

import pygame
import random

# self.bird_rect represents the rectangle surrounding the bird image. These rectangles will be used for collision detection.
class Game:
  
  def __init__(self, bird_img, pipe_img, background_img, ground_img):
    self.bird = pygame.image.load(bird_img).convert_alpha()
    # convert_alpha() -> 
    self.bird_rect = self.bird.get_rect(center = (70, 160))
    self.pipe = pygame.image.load(pipe_img).convert_alpha()
    self.background = pygame.image.load(background_img).convert_alpha()
    self.ground = pygame.image.load(ground_img).convert()
    self.ground_position = 0
    self.active = True
    self.gravity = 0.03
    self.bird_movement = 0
    self.rotated_bird = pygame.Surface((0, 0))
    self.pipes =[]
    self.pipe_height =[280, 425, 562]
    self.score = 0
    self.font = pygame.font.SysFont(None, 48)
    self.high_score = 0
    self.lifes = 0 

    
    
  


  def resize_images(self):
    self.bird = pygame.transform.scale(self.bird, (51, 34))
    self.pipe = pygame.transform.scale(self.pipe, (80, 438))
    self.ground = pygame.transform.scale(self.ground, (470, 160))
    self.background = pygame.transform.scale(self.background, (400, 720))

  def show_background(self, screen):
    screen.blit(self.background, (0,0)) 
    # blit method, which stands for Bit Block Transfer. Bit Block Transfers move pixels to a location on the screen. 

  def add_pipe(self):
    selected_pipe_height = random.choice(self.pipe_height)
    bottom_pipe = self.pipe.get_rect(midtop = (450, selected_pipe_height))
    top_pipe = self.pipe.get_rect(midbottom = (450, selected_pipe_height - 211))
    self.pipes.append(bottom_pipe)
    self.pipes.append(top_pipe)


  def move_pipes(self):
    for pipe in self.pipes:
        pipe.centerx -= 1.75
        # centerx > x-axes
        if pipe.centerx <= 40:
            self.pipes.remove(pipe)         

  def show_pipes(self, screen):
    for pipe in self.pipes:
        if pipe.top <0:
            flip_pipe = pygame.transform.flip(self.pipe, False, True)
            screen.blit(flip_pipe, pipe)
        else:
            screen.blit(self.pipe, pipe)         
  
  def show_ground(self,screen):
    screen.blit(self.ground,(self.ground_position,550)) 
    # screen.blit(self.ground, (self.ground_position + 470, 650))
    self.ground_position -= 1
    if self.ground_position <-70:
      self.ground_position =0
    

#   def move_ground(self):
#     self.ground_position -= 1
#     if self.ground_position <= -400:
#       self.ground_position = 0

#######  the bird methods ###########

  def show_bird(self,screen):
      screen.blit(self.rotated_bird, self.bird_rect)

  def update_bird(self):
    self.bird_movement += self.gravity
    self.bird_rect.centery += self.bird_movement
    self.rotated_bird = self.rotate_bird()   

  def rotate_bird(self):
    new_bird = pygame.transform.rotozoom(self.bird,-self.bird_movement * 3, 1)
    # angle  of the bird -self.bird_movement * 5 making it postive mean the rotation will be to the up and negtive will make the bird rotated down 
    # rotozoom(surface, angle, scale) -> Surface
    # rotozoom >> This is a combined scale(in this case I am not using the scale par) and rotation transform
    return new_bird 
  
  def flap(self):
    self.bird_movement = 0
    if self.bird_rect.y > 50 :
     self.bird_movement -= 1.2 

#######  collision  ###########

  def check_collision(self):
    if self.bird_rect.top >= 550 or self.bird_rect.bottom < -1:
       self.active =False
    for pipe in self.pipes:
       if self.bird_rect.colliderect(pipe):
        self.active =False   

#######  scores  ###########

  def update_score(self):
    self.score += 0.01

  def show_score(self, game_state, screen, color):  
    if game_state == 'playing':
     score_surface = self.font.render(str(int(self.score)), True, color)
      #  render(test, antialias , color)
     # Antti-aliasing is a computer graphics technique that smoothes jagged edges on curves and diagonal lines
     score_rect = score_surface.get_rect(center=(202, 75))
     screen.blit(score_surface, score_rect)

    elif game_state == 'game_over':
      
     restart_text1 = self.font.render('Press Space Bar', True, color)
     restart_rect1 = restart_text1.get_rect(center=(200, 280))
     screen.blit(restart_text1, restart_rect1)
      
     restart_text2 = self.font.render('to Play Again', True, color)
     restart_rect2 = restart_text2.get_rect(center=(200, 340))
     screen.blit(restart_text2, restart_rect2)

     high_score_surface = self.font.render('High Score: {:d}'.format(int(self.high_score)), True, color)
     high_score_rect = high_score_surface.get_rect(center=(200, 610))
     screen.blit(high_score_surface, high_score_rect)
      


####### game_over ######## 

  def game_over(self,screen,color):
    self.update_high_score()
    self.show_score('game_over', screen, color)

  def update_high_score(self):
   if self.score > self.high_score:
     self.high_score = self.score

  def restart(self):
    if self.lifes < 2:
        self.active = True
        self.score = 0
        del self.pipes[:]
        self.bird_rect.center = (70, 180)
        self.bird_movement = 0
        self.rotated_bird = pygame.Surface((0, 0))
        self.lifes+=1
 

  def end_of_life_screen(self,screen):
      screen.blit(self.background, (0,0)) 
      trys_end_surface = self.font.render('End Game ', True, (255,255,255))
      trys_end_rect= trys_end_surface.get_rect(center=(200, 280))
      screen.blit(trys_end_surface, trys_end_rect)        



      