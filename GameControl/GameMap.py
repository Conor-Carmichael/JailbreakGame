from GlobalValues import *
from lib import encode_point

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


    def create_map(self, display_surface):
        enemy_spawns = []
        m = open(self.map_file, 'r')
        rows = m.readlines()
        self.height = len(rows)
        self.width = len(rows[0])
        for y, row in enumerate(rows):
            for x, pixel in enumerate(row):

                if pixel != '\n' and pixel in MAP_KEYS.keys():
                    display_surface.set_at((x, y), COLORS[MAP_KEYS[pixel]])
                    if pixel == 'w':
                        self.obstructions[encode_point((x,y))] = True
                    # elif pixel == '/'
        print(self.obstructions)
        m.close()
        # return enemy_spawns, player_spawn, key_loc, walls


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