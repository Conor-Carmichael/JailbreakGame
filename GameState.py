# from Positioning import equals
from copy import deepcopy
from GlobalValues import *


class GameState:

    """ Data structure to hold all knowledge about the game """
    """ Might be glorified dict, but deepcopys              """

    def __init__(self, enemies ): #protagonist, game_key):
        # self.state_dict = {protagonist.id: deepcopy(protagonist.position)}
        self.state_dict = {}
        for e in enemies:
            self.state_dict[e.id] = [deepcopy(e.get_loc()), deepcopy(e.get_flashlight_points(ENEMY_FLASHLIGHT_MULTIPLIER))]

    def get(self, id):
        return self.state_dict[id]

    def update(self, key, val):
        self.state_dict[key] = deepcopy(val)
    
    # def pos_changed(self, key, val):
    #     return equals(self.state_dict[key], val)
        
