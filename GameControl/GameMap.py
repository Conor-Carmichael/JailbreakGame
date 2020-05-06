from GlobalValues import *
from lib import encode_point

import os, json, pygame
import numpy as np


class GameMap(pygame.sprite.Sprite):

    def __init__(self, map_file):
        #Necessary sprite super call
        pygame.sprite.Sprite.__init__(self)
        
        # Info used for further setup
        img_path = os.path.join(MAP_IMAGES_PATH, map_file)
        info_path =  os.path.join(MAP_INFO_PATH, map_file) #store because it is used in parse map info
        info_path = info_path[:-4]+'.json' #remove .png, use .json

        #Sprite info    
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()

        #Map dimens
        self.width = self.rect[2]
        self.height = self.rect[3]
        print(self.width, self.height)

        #Map locations 
        self.protagonist_spawn, self.enemy_spawns, self.key_spawn, self.door_span = self.parse_map_info(info_path)
        self.obstructions = self.set_obstruction_list()

        self.num_enemies = len(self.enemy_spawns)


    def parse_map_info(self, fp):
        # to run in init
        info = open(fp, )
        info = json.load(info)
        #Coordinates are in the form y, x
        protagonist_spawn = info['protagonist_spawn']
        enemy_spawns = info['enemy_spawns']
        key_spawn = info['key_spawn']
        door_span = info['door_span']
        return protagonist_spawn, enemy_spawns, key_spawn, door_span

    def set_obstruction_list(self):
        obst = {}
        for x in range(self.width):
            for y in range(self.height):
                val = self.image.get_at((x,y))
                if val == COLORS['wall']:
                    obst[encode_point((x,y))] = True

        return obst


    def get_color_at(xy):
        x, y = xy
        return self.width * y + x

    def in_bound(self, xy):
        x, y = xy
        return x >= 0 and y >= 0 and x < self.width and y < self.height
           
    def not_obstructed(self, xy):
        # print(self.obstructions)
        if self.obstructions.get(encode_point(xy)):
            print('obst: ', xy)
            return False
        else:
            return True
