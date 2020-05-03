from copy import deepcopy
from Characters.Enemy import Enemy
from GlobalValues import *
from lib import *


class GameState:

    def __init__(self, enemies, protagonist, key): #protagonist, game_key):
        # self.state_dict = {protagonist.id: deepcopy(protagonist.position)}
        self.character_locations, self.light_locations = {}, {}
        self.character_locations[protagonist.id] = deepcopy(protagonist.get_loc())
        for e in enemies:
            self.character_locations[e.id] = deepcopy(e.get_loc())
            self.light_locations[e.id+'-light'] = deepcopy(e.get_flashlight_points(ENEMY_FLASHLIGHT_MULTIPLIER))
        
        self.key = key
        self.protagonist = protagonist
        self.enemies = enemies
        # Game state vars like timer, has_ley


    def get_character_loc(self, id):
        return self.character_locations[id]

    def get_enemy_light_loc(self, enemy_id):
        return self.light_locations[enemy_id+'-light']


    def update_loc(self, key, val):
        self.character_locations[key] = deepcopy(val)
    
    def update_light(self, key, val):
        self.light_locations[key+'-light'] = deepcopy(val)


    def protagonist_caught(self):
        main_area = None
        protag_loc = self.character_locations['protagonist'] 
        # Do not do calculations if protagonist is further than SIGHT_RANGE
        for i in range(Enemy.enemy_count):
            sight = self.light_locations['enemy-'+str(i)+'-light']
            if distance(self.get_character_loc('enemy-'+str(i)), protag_loc) <= FLASHLIGHT_RANGE:
                for corner in get_corner_coords(protag_loc[0], protag_loc[1], self.protagonist.size): # Check if corners are in sight
                    result, main_area = is_inside_triangle(sight, protag_loc, main_area)
                    if result:
                        print('Corner contact at ', corner, ' location ', protag_loc)
                        print(sight)
                        return True
        
        return False
        


    def key_collected(self):
        return