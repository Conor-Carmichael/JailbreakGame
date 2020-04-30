import pygame, sys, random, os
import numpy as np
from Character import  Character
from Enemy import Enemy
from Positioning import Positioning
# import Character, Positioning, Enemy

from pygame.locals import *



pygame.init()

#Important Variables 
RESOLUTION = (1280, 720)
UP, DOWN, LEFT, RIGHT = 'UP','DOWN','LEFT','RIGHT'
FPS = 60
DISPLAY_SURFACE = pygame.display.set_mode(RESOLUTION, 0, 32)



pygame.display.set_caption('Jailbreak!')
fpsClock = pygame.time.Clock()

#Coordinate grid to use in calculating enemy field of view
coord_grid = []
for row in range(RESOLUTION[0]):
    cg_row = []
    for col in range(RESOLUTION[1]):
        cg_row.append((row, col))
    coord_grid.append(cg_row)
coord_grid = np.asarray(coord_grid)


# colors = {
#     'k': (0,0,0),
#     'w': (255,255,255, 100),
#     'flashlight': 
# }

DISPLAY_SURFACE.fill(colors['w'])

#Creating characters

enemy_one_start_pos = Positioning(100, 100, DOWN)
enemy_two_start_pos = Positioning(100, 400, DOWN)

enemy_one = Enemy(0, 90, enemy_one_start_pos, 10, None)
enemy_two = Enemy(0, 90, enemy_two_start_pos, 10, None)


user_start_pos = Positioning(400, 500, UP)
user_img = pygame.image.load('Images/Protagonist_upsc.png')
user_character = Character(user_start_pos, 10, None)



pix_obj = pygame.PixelArray(DISPLAY_SURFACE)


for vision in enemy_two.get_fov(coord_grid):
    # Would filter out elements of the map first
    pix_obj[vision[1]][vision[0]] = colors['flashlight'] #Reversed?

del pix_obj # Unlock board

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    row, col = user_character.get_pos().get_coords()

    DISPLAY_SURFACE.blit(user_img, (row, col))

    pygame.display.update()
    fpsClock.tick(FPS)