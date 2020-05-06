import pygame, sys, random, os
import numpy as np
from pygame.locals import *

# My Files
from lib import *
from GlobalValues import *

from Characters.Character import  Character
from Characters.Protagonist import  Protagonist
from Characters.Flashlight import  Flashlight
from Characters.Enemy import Enemy

from GameControl.Positioning import Positioning
from GameControl.GameState import GameState
from GameControl.GameMap import GameMap


class JailbreakGame:

    """                Class to control the Jailbreak Game                   """
    """  Code for game management, that is universal (ie not map dependent)  """

    def __init__(self, resolution, fps):

        self.resolution = resolution
        self.fps = fps
        self.pause = False
        self.camera = None


    def setup(self):
        # Does the every-match setup and initialization
        pygame.init()
        DISPLAY_SURFACE = pygame.display.set_mode(self.resolution)

        pygame.display.set_caption('Jailbreak!')
        fpsClock = pygame.time.Clock()
        
        return DISPLAY_SURFACE, fpsClock

    def run(self, display, enemy, fps_clock, fps, map):
        return

    def init_map(self, map_file, display, game_state):
        game_map = GameMap(map_file)
        self.enemies = self.create_enemies(count=game_map.num_enemies, spawn_seeds=game_map.enemy_spawns)

        light_points = [e.get_flashlight_points() for e in self.enemies]
        self.flashlights = self.create_enemy_flashlight(light_points, display)

        prot_start = Positioning(game_map.protagonist_spawn[0], game_map.protagonist_spawn[1], RIGHT)
        self.protagonist = Protagonist(prot_start, PROTAGONIST_IMAGE)
        self.game_map = game_map # Just to avoid all the self calls above, wait to set it

        #When creating flashlights they immediately get drawn, so they are skipped here
        for to_blit in [self.game_map, self.protagonist, *self.enemies]:
            display.blit(to_blit.image, to_blit.rect)        

    
    def create_enemies(self, count=1, spawn_seeds=None):
        #Spawn seeds: arr of tuples, (mean x, mean y)
        enemies = []
        for i in range(count):
            e_pos = Positioning(spawn_seeds[i][0], spawn_seeds[i][1], UP)
            e = Enemy(FLASHLIGHT_RANGE, e_pos, ENEMY_IMG)
            enemies.append(e)

        return enemies

    def create_enemy_flashlight(self, points, display_surface):
        flashlights = []
        
        for p_set in points:
            f = Flashlight(display_surface, p_set)
            flashlights.append(f)

        return flashlights

    def control_handler(self, pressed):
        # Returns True if user moved
        if pressed[pygame.K_w]:
            self.protagonist.turn(UP)
            return self.protagonist.move(self.game_map)

        elif pressed[pygame.K_a]:
            self.protagonist.turn(LEFT)
            return self.protagonist.move(self.game_map)

        elif pressed[pygame.K_s]:
            self.protagonist.turn(DOWN)
            return self.protagonist.move(self.game_map)

        elif pressed[pygame.K_d]:
            self.protagonist.turn(RIGHT)
            return self.protagonist.move(self.game_map)

        else:
            return False


    def game_over_screen(self):
        return None

    def title_screen(self):
        return

# Using to test everything
if __name__ == '__main__':


    Jailbreak = JailbreakGame(RESOLUTION_OPTIONS[2], FPS_OPTIONS[2])
    display_surface, fps_clock = Jailbreak.setup()
    Jailbreak.init_map(MAP_FILE_NAMES[0], display_surface, None)

    game_state = GameState(Jailbreak.enemies, Jailbreak.flashlights, Jailbreak.protagonist, None)

    while True:
        # # good line from tutorial: sprites_clicked = [sprite for sprite in all_my_sprites_list if sprite.rect.collidepoint(x, y)]


        for event in pygame.event.get():
            # event_handler(event)
            if event.type == QUIT or game_state.protagonist_caught():
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        Jailbreak.control_handler(keys) 

        for e in Jailbreak.enemies:
            e.chance_turn()
            e.chance_move(Jailbreak.game_map)
            
        for to_blit in [Jailbreak.game_map, Jailbreak.protagonist, *Jailbreak.enemies]:
            display_surface.blit(to_blit.image, to_blit.rect)

        for e, f in zip(Jailbreak.enemies, Jailbreak.flashlights):
            f.new_points(e.get_flashlight_points(), display_surface)
            
        pygame.display.update() 
        fps_clock.tick(Jailbreak.fps)
               
