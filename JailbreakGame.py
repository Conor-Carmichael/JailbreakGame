import pygame, sys, random, os
import numpy as np
from pygame.locals import *

# My Files
from GlobalValues import *
from Characters.Character import  Character
from Characters.Enemy import Enemy
from GameControl.Positioning import Positioning
from GameControl.GameState import GameState

# import time


class JailbreakGame:

    """ Class to control the Jailbreak Game """
    """   """

    def __init__(self, resolution):

        self.resolution = resolution
        self.enemies = []
        self.protagonist = None

    def setup(self):
        # Does the every-match setup and initialization
        pygame.init()
        DISPLAY_SURFACE = pygame.display.set_mode(RESOLUTION_OPTIONS[0])

        pygame.display.set_caption('Jailbreak!')
        fpsClock = pygame.time.Clock()
        
        return DISPLAY_SURFACE, fpsClock

    def run(self, display, enemy, fps_clock, fps):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # row, col = user_character.get_loc().get_coords()

            # display.blit(user_img, (row, col))

            pygame.display.update()
            fps_clock.tick(fps)
    
    def create_map(self):
        return

        
    def create_enemies(self, count=1, spawn_seeds=None):
        #Spawn seeds: arr of tuples, (mean x, mean y)
        enemies = []
        for i in range(count):
            e_pos = Positioning()
            e_dir = None
            if spawn_seeds and spawn_seeds[i]:
                e_pos.set_rand(spawn_seeds[i][0], spawn_seeds[i][1], int(self.resolution[0]/100))
                e_dir = spawn_seeds[i][2]
            e = Enemy(FLASHLIGHT_RANGE, e_pos, ENEMY_IMG)
            e.position.print_pos()
            enemies.append(e)

        self.enemies = enemies


    def update(self, display_surface, game_state, new_state):
        # new state values are the character and the type of character
        for character in new_state.values():
            #Get location to erase
            old_loc = game_state.get(character.id)[0] 
            old_rect = character.image.get_rect()
            to_erase = (old_rect[0] + old_loc[0], old_rect[1] + old_loc[1], old_rect[2] + old_loc[0],  old_rect[3] + old_loc[1]) 

            pygame.draw.polygon(display_surface, COLORS['background'], game_state.get(character.id)[1])  # Erase old light
            display_surface.fill(COLORS['background'], to_erase) # Erase at old enemy points
            
            display_surface.blit(character.image, character.get_loc())          #Draw new enemy
            if True: # Need to check if its a enemy to draw light
                pygame.draw.polygon(display_surface, COLORS['flashlight'], character.get_flashlight_points(ENEMY_FLASHLIGHT_MULTIPLIER))

    # Checks to make sure not going out of bounds of screen
    def point_in_bound(self, xy):
        x, y = xy # Pass as Tuple
        return x in range(0, self.resolution[0]) and y in range(0, self.resolution[1]) 

    # Game state methods
    def protagonist_is_caught(self):
        return False

    def is_winning_state(self):
        # has key, and is in doorway
        return False





# enemy_light = pygame.draw.polygon(display, COLORS['flashlight'], enemy_one.get_flashlight_points(0.5))


# Using to test everything
if __name__ == '__main__':
    res = RESOLUTION_OPTIONS[0]
    game = JailbreakGame(res)
    display_surface, fps_clock = game.setup()

    display_surface.fill(COLORS['background'])
    game.create_enemies(count=2, spawn_seeds=[(400, 500, 2), (900, 100, 3)])

    game_state = GameState(game.enemies)

    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # if wasd move user? Mouse click would be better (league style)

        # Check for updates       
        changes = {}
        # Check user changes:

        #Check enemy changesd
        for e in game.enemies:
            e_turned = e.chance_turn()
            if e.chance_move(game.resolution):
                changes[e.id] = e #Store character to update

        game.update(display_surface, game_state, changes) #Visually update player locations

        for k,v in changes.items(): #Store the new game state
            #If enemy:
            game_state.update(k, [v.get_loc(), v.get_flashlight_points()])

        pygame.display.update()
        fps_clock.tick(FPS_OPTIONS[2])


    
