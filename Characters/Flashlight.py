import pygame
from GlobalValues import *

class Flashlight(pygame.sprite.Sprite):

    def __init__(self, display, points):
        pygame.sprite.Sprite.__init__(self)
        self.points = points
        self.rect = pygame.draw.polygon(display, COLORS['flashlight'], points)

    def new_points(self, points, display):
        self.points = points
        self.rect = pygame.draw.polygon(display, COLORS['flashlight'], points)
