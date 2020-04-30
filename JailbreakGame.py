import pygame, sys, random, os
from pygame.locals import *



class JailbreakGame:

    """ Class to control the Jailbreak Game """

    def __init__(self, protagonist, enemies, resolution, fps):
        self.enemies = enemies
        self.resolution = resolution
        self.fps = fps

        self.colormap = {
            'background': (0,0,0),
            'obstacle': (),
            'wall': ()
            'flashlight': (100, 150, 0),
        }

        # pygame.init()
        # self.DISPLAY_SURFACE = pygame.display.set_mode(self.resolution, 0, 32)
        # pygame.display.set_caption('Jailbreak!')
        # fpsClock = pygame.time.Clock()


    def create_map(self):
        return

    def color_enemy_fov(self):
        return
    
    def protagonist_is_caught(self):
        return False

    def is_winning_state(self):
        return False

    def update_environment(self):
        # Make enemies moves, turns



    def run(self):
        # pygame.display.set_caption('Jailbreak!')
        # fpsClock = pygame.time.Clock()