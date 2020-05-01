import pygame, sys, random, os
from pygame.locals import *
import numpy as np

from Character import  Character
from Enemy import Enemy
from Positioning import Positioning

from GlobalValues import *




pygame.init()

#Important Variables 
RESOLUTION =RESOLUTION_OPTIONS[0]
FPS = 60
DISPLAY_SURFACE = pygame.display.set_mode(RESOLUTION, 0, 32)



pygame.display.set_caption('Jailbreak!')
fpsClock = pygame.time.Clock()


DISPLAY_SURFACE.fill(COLORS['background'])

#Creating characters

enemy_one_start_pos = Positioning()
enemy_two_start_pos = Positioning()

enemy_one_start_pos.set_rand(100, 200, 25)
enemy_two_start_pos.set_rand(100, 200, 25)


enemy_img = pygame.image.load('Images/Enemy.png')

enemy_one = Enemy(0, 0, 90, enemy_one_start_pos, enemy_img)
enemy_two = Enemy(0, 0, 90, enemy_two_start_pos, enemy_img)

DISPLAY_SURFACE.blit(enemy_one.image, enemy_one.get_pos())
DISPLAY_SURFACE.blit(enemy_two.image, enemy_two.get_pos())



print(enemy_one.id, enemy_two.id)

# user_start_pos = Positioning(400, 500, UP)
# user_img = pygame.image.load('Images/Protagonist_upsc.png')
# user_character = Character(user_start_pos, 10, None)



# pix_obj = pygame.PixelArray(DISPLAY_SURFACE)


# for vision in enemy_one.get_fov():
#     # Would filter out elements of the map first
#     pix_obj[vision[1]][vision[0]] = COLORS['flashlight'] #Reversed?

# del pix_obj # Unlock board

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)