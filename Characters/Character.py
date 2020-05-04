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


    def __init__(self, position, image):
        self.position = position                #Positioning Object
        self.image = pygame.image.load(image)  #Image to repr character
        image_rect = self.image.get_rect()
        self.size = (image_rect[2], image_rect[3])



    def valid_move(self, new_coords, map_bounds):
        new_x, new_y = new_coords
        x_lim, y_lim = map_bounds

        if new_x+self.size[0] >= x_lim or new_x < 0 or new_y+self.size[1] >= y_lim or new_y < 0:
            return False
        else:
            return True

    def move(self, game_map):
        x, y, d = self.position.get()

        if d==RIGHT:
            # dont if x + step + width > bound[0]
            relev_bound = (x + STEP + self.size[0], y)

            if game_map.in_bound(relev_bound) and game_map.not_obstructed(relev_bound):
                self.position.update_x(x+STEP)
        elif d==LEFT:
            relev_bound = (x - STEP, y)
            if game_map.in_bound(relev_bound) and game_map.not_obstructed(relev_bound):
                self.position.update_x(x-STEP)
        elif d==DOWN:
            relev_bound = (x, y + STEP + self.size[1])
            if game_map.in_bound(relev_bound) and game_map.not_obstructed(relev_bound):
                self.position.update_y(y+STEP)
        elif d==UP:
            relev_bound = (x, y - STEP)
            if game_map.in_bound(relev_bound) and game_map.not_obstructed(relev_bound):
                self.position.update_y(y-STEP)

        

    def turn(self, new_dir):
        self.position.update_direction(new_dir)
    
    def get_loc(self):
        return self.position.get_coords()
        
    def get_dir(self):
        return self.position.get_direction()
        