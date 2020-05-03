from GlobalValues import *


class GameMap:

    def __init__(self, map_file, display_surface):
        self.map_file = map_file
        self.display_surface = display_surface
        self.protagonist_spawn = None
        self.enemy_spawns = None
        self.key_loc = None
        self.door_loc = None
        self.create_map()

    def create_map(self):
        enemy_spawns = []
        m = open(self.map_file, 'r')
        rows = m.readlines()

        for y, row in enumerate(rows):
            for x, pixel in enumerate(row):
                if pixel != '\n' and pixel in MAP_KEYS.keys():
                    self.display_surface.set_at((x, y), COLORS[MAP_KEYS[pixel]])
        m.close()

        # return enemy_spawns, player_spawn, key_loc, walls
