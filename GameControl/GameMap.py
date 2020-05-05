from GlobalValues import *
from lib import encode_point
import numpy as np

class GameMap:

    def __init__(self, map_file):
        self.map_file = map_file

        # Rest set by call to 'create_map()'
        #map dimens
        self.width = None
        self.height = None

        #Map locations
        self.protagonist_spawn = None
        self.enemy_spawns = None
        self.key_loc = None
        self.door_loc = None
        self.obstructions = {}
        self.map_coloring = {}

    def create_map(self, display_surface):
        enemy_spawns = []
        m = open(self.map_file, 'r')
        rows = m.readlines()
        self.height = len(rows)
        self.width = len(rows[0])

        self.map_coloring = np.arange(self.width*self.height)

        for y, row in enumerate(rows):
            for x, pixel in enumerate(row):
                if pixel != '\n' and pixel in MAP_KEYS.keys():

                    pix_color = COLORS[MAP_KEYS[pixel]]
                    # self.map_coloring[self.width * y + x] = pix_color
                    display_surface.set_at((x, y), pix_color)

                    if pixel == '#':
                        self.obstructions[encode_point((x,y))] = True
                    
        m.close()
        # return enemy_spawns, player_spawn, key_loc, walls


    # def recolor_tri()

    # def recolor_rect(self, disp, rect):
    #     x1, y1, width, height = rect 
    #     for x in range(x1, x1+width+1):
    #         for y in range(y1, y1+height+1):
    #             disp.set_at((x,y), self.get_color_at((x,y)))

    def get_color_at(xy):
        x, y = xy
        return self.width * y + x

    def in_bound(self, xy):
        x, y = xy
        return x >= 0 and y >= 0 and x < self.width and y < self.height
           
    def not_obstructed(self, xy):
        # print(self.obstructions)
        if self.obstructions.get(encode_point(xy)):
            # print('obst: ', xy)
            return False
        else:
            return True
