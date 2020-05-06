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

class Character(pygame.sprite.Sprite):


    def __init__(self, position, image):
        pygame.sprite.Sprite.__init__(self)

        self.position = position                   #Positioning Object
        self.image = pygame.image.load(image)      #Image to repr character
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position.get_coords()
        self.size = (self.rect[2], self.rect[3])

        self.in_motion = False  # Keyboard input sets this    


    def set_in_motion(self):
        self.in_motion = True

    def stop_movement(self):
        self.in_motion = False


    def move(self, game_map):
        # For each step: 
        # Check if in bounds of map width/height 
        # Check if new loc is not obstructed by walls etc
        # -> if right need to check top right, and bot right, so on so forth
        # **return True if the move was executed, else False
        _, _, d = self.position.get()
        x, y = self.rect[0], self.rect[1]

        if d==RIGHT:
            # dont if x + step + width > bound[0]
            relev_bound = (x + STEP + self.size[0], y)
            other_relev = (x + STEP + self.size[0], y+self.size[1])
            if game_map.in_bound(relev_bound) and game_map.not_obstructed(relev_bound) and game_map.not_obstructed(other_relev):
                self.rect.move_ip((STEP, 0))
                return True            

        elif d==LEFT:
            relev_bound = (x - STEP, y)
            other_relev = (x - STEP, y+self.size[1])
            if game_map.in_bound(relev_bound) and game_map.not_obstructed(relev_bound) and game_map.not_obstructed(other_relev):
                self.rect.move_ip((-1*STEP, 0))
                return True            

        elif d==DOWN:
            relev_bound = (x, y + STEP + self.size[1])
            other_relev = (x + self.size[0], y + STEP + self.size[1])
            if game_map.in_bound(relev_bound) and game_map.not_obstructed(relev_bound) and  game_map.not_obstructed(other_relev):
                self.rect.move_ip((0, STEP))
                return True 
                
        elif d==UP:
            relev_bound = (x, y - STEP)
            other_relev = (x+self.size[0], y - STEP)
            if game_map.in_bound(relev_bound) and game_map.not_obstructed(relev_bound) and game_map.not_obstructed(other_relev):
                self.rect.move_ip((0, -1*STEP))
                return True 

        # The move was not able to be executed
        return False

    def turn(self, new_dir):
        self.position.update_direction(new_dir)
    
    def get_loc(self):
        return self.position.get_coords()
        
    def get_dir(self):
        return self.position.get_direction()
        