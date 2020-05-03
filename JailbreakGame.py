import pygame, sys, random, os
import numpy as np
from pygame.locals import *

# My Files
from lib import *
from GlobalValues import *
from Characters.Character import  Character
from Characters.Protagonist import  Protagonist
from Characters.Enemy import Enemy
from GameControl.Positioning import Positioning
from GameControl.GameState import GameState
from GameControl.GameMap import GameMap

# import time


class JailbreakGame:

    """                Class to control the Jailbreak Game                   """
    """  Code for game management, that is universal (ie not map dependent)  """

    def __init__(self, resolution):

        self.resolution = resolution
        self.enemies = []
        self.protagonist = None


    def setup(self):
        # Does the every-match setup and initialization
        pygame.init()
        DISPLAY_SURFACE = pygame.display.set_mode(self.resolution)

        pygame.display.set_caption('Jailbreak!')
        fpsClock = pygame.time.Clock()
        
        return DISPLAY_SURFACE, fpsClock

    def run(self, display, enemy, fps_clock, fps):
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

    def control_handler(self, pressed, user):
        # Returns True if user moved
        if pressed[pygame.K_w]:
            user.turn(UP)
            user.move(self.resolution)
            return True
        elif pressed[pygame.K_a]:
            user.turn(LEFT)
            user.move(self.resolution)
            return True
        elif pressed[pygame.K_s]:
            user.turn(DOWN)
            user.move(self.resolution)
            return True
        elif pressed[pygame.K_d]:
            user.turn(RIGHT)
            user.move(self.resolution)
            return True
        else:
            return False

    def redraw(self, display_surface, game_state, new_state):
        # new state values are the character and the type of character
        for character in new_state.values():
            #Get location to erase
            old_loc = game_state.get_character_loc(character.id)
            to_erase = (old_loc[0] , old_loc[1], character.size[0], character.size[1])

            display_surface.fill(COLORS['floor'], to_erase) # Erase at old character

            if 'enemy' in character.id:
                pygame.draw.polygon(display_surface, COLORS['floor'], game_state.get_enemy_light_loc(character.id))  # Erase old light
                new_light_points = character.get_flashlight_points(ENEMY_FLASHLIGHT_MULTIPLIER)
                pygame.draw.polygon(display_surface, 
                                    COLORS['flashlight'], 
                                    new_light_points) # Draw new light
                game_state.update_light(character.id, new_light_points)
            
            display_surface.blit(character.image, character.get_loc()) #Draw new character
            game_state.update_loc(character.id, character.get_loc())




# Using to test everything
if __name__ == '__main__':
    res = RESOLUTION_OPTIONS[2]
    game = JailbreakGame(res)
    display_surface, fps_clock = game.setup()

    # display_surface.fill(COLORS['floor'])
    game_map = GameMap('./GameControl/Maps/map_one.txt', display_surface)

    game.create_enemies(count=2, spawn_seeds=[(400, 500, 2), (900, 100, 3)])
    prot_pos = Positioning(100, 100, RIGHT)
    protagonist = Protagonist(prot_pos, PROTAGONIST_IMAGE)
    game_state = GameState(game.enemies, protagonist, None)
    protag_loc = protagonist.get_loc()
    print('PROTAG BOUND: ', get_corner_coords(protag_loc[0], protag_loc[1], protagonist.size))
    while True:

        prot_moved = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        prot_moved = game.control_handler(keys, protagonist)


        # Check for updates       
        changes = {}

        # Check user changes:
        if prot_moved:
            changes[protagonist.id] = protagonist

        #Check enemy changesd
        for e in game.enemies:
            e_turned = e.chance_turn()
            if e.chance_move(game.resolution):
                changes[e.id] = e #Store character to update                


        game.redraw(display_surface, game_state, changes) #Visually update player locations
        if game_state.protagonist_caught():
            print("GAME OVER")
            quit()

        pygame.display.update()
        fps_clock.tick(FPS_OPTIONS[2])


    
