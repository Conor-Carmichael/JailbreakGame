import pygame, sys, random, os
import numpy as np
from pygame.locals import *

# My Files
from global_values import *
from Character import  Character
from Enemy import Enemy
from Positioning import Positioning
import time
class JailbreakGame:

    """ Class to control the Jailbreak Game """

    def __init__(self, resolution):

        self.resolution = resolution
        self.width = self.resolution[1]
        self.height = self.resolution[0]
        # self.fps = fps


    def create_map(self):

        return

     
    # Checks to make sure not going out of bounds to highlight
    def valid_fov(self, val):
        #val[0] = y val; val[1] = x
        # first is row, second is col
        # print(val, res)
        # b
        return val[0] in range(0, self.resolution[1]) and val[1] in range(0, self.resolution[0]) 


    def color_enemy_fov(self, display, enemy, color):
        pix_obj = pygame.PixelArray(display)
        fov = enemy.get_fov()
        print('Retrieved fov, size: ', len(fov))
        for visible in fov:
            # Would filter out elements of the map first
            if self.valid_fov(visible):
                pix_obj[visible[1]][visible[0]] =  color #Reversed?
            else:
                print('Invalid ', visible)

        del pix_obj # Unlock board

        return True
    
    def protagonist_is_caught(self):
        return False

    def is_winning_state(self):
        return False

    def update_environment(self):
        # Make enemies moves, turns
        return





    def setup(self):
        # Does the every-match setup and initialization
        pygame.init()
        DISPLAY_SURFACE = pygame.display.set_mode(RESOLUTION_OPTIONS[0], 0, 32)

        pygame.display.set_caption('Jailbreak!')
        fpsClock = pygame.time.Clock()
        
        return DISPLAY_SURFACE, fpsClock

    def run(self, display, enemy, fps_clock, fps):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # row, col = user_character.get_pos().get_coords()

            # display.blit(user_img, (row, col))

            pygame.display.update()
            fps_clock.tick(fps)


# Using to test everything
if __name__ == '__main__':
    res = RESOLUTION_OPTIONS[0]
    game = JailbreakGame(res)
    display, fps_clock = game.setup()

    enemy_pos = Positioning(x=300, y=300, d=RIGHT)
    enemy_one = Enemy(0.0, 0.0, 100, enemy_pos, 10, None)
    # game.run(display, enemy_one, fps_clock, 30)
    while True:
        enemy_light = pygame.draw.polygon(display, COLORS['flashlight'], enemy_one.get_flashlight_points(0.5))
        
        # for d in DIRECTIONS: 
        #     enemy_one.turn(d)
        #     enemy_light.move_ip(enemy_one.get_flashlight_points(0.5))


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        # row, col = user_character.get_pos().get_coords()
        # display.blit(user_img, (row, col))
        # print()
        pygame.display.update()
        fps_clock.tick(30)


    
