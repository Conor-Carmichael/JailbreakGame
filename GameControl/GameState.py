# from Positioning import equals
from copy import deepcopy
from GlobalValues import *


class GameState:

    def __init__(self, enemies, protagonist, key): #protagonist, game_key):
        # self.state_dict = {protagonist.id: deepcopy(protagonist.position)}
        self.character_locations = {}
        self.character_locations[protagonist.id] = deepcopy(protagonist.get_loc())
        for e in enemies:
            self.character_locations[e.id] = deepcopy(e.get_loc())
            self.character_locations=[e.id+'-light'] = deepcopy(e.get_flashlight_points(ENEMY_FLASHLIGHT_MULTIPLIER))
        
        self.key = key
        # Game state vars like timer, has_ley


    def get_character_locations(self):
        return self.character_locations

    def update(self, key, val):
        self.state_dict[key] = deepcopy(val)
    
    # def pos_changed(self, key, val):
    #     return equals(self.state_dict[key], val)
        
    def key_collected(self):
        return