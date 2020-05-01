#################################################################
#                                                               #
#                                                               #
#        The main Character class in the jaibreak game.         #
#        Extended to make enemy and main character classes      #
#                                                               #
#                                                               #
#################################################################
import pygame
from GlobalValues import *


class Character:

    char_id = 0

    def __init__(self, position, image):
        self.position = position                #Positioning Object
        self.image = pygame.image.load(image)                      #Image to repr character
        self.id = Character.char_id             # id stores the item in gamestate
        Character.char_id += 1


    def valid_move(self, new_coords, map_bounds):
        new_x, new_y = new_coords
        x_lim, y_lim = map_bounds

        if new_x+self.size[0] >= x_lim or new_x < 0 or new_y+self.size[1] >= y_lim or new_y < 0:
            return False
        else:
            return True

    def move(self):
        x, y, d = self.position.get() # Row, Column, Direction

        if d==RIGHT:
            self.position.update_x(x+STEP)
        elif d==LEFT:
            self.position.update_x(x-STEP)
        elif d==DOWN:
            self.position.update_y(y+STEP)
        elif d==UP:
            self.position.update_y(y-STEP)

    def turn(self, new_dir):
        self.position.update_direction(new_dir)
    
    def get_loc(self):
        return self.position.get_coords()
        
    def get_dir(self):
        return self.position.get_direction()
        