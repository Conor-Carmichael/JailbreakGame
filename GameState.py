from Positioning import equals
from copy import deepcopy

class GameState:

    """ Data structure to hold all knowledge about the game """
    """ Might be glorified dict, but deepcopys              """

    def __init__(self, enemies, protagonist, game_key):
        self.state_dict = {protagonist.id: deepcopy(protagonist.position)}
        for e in enemies:
            state_dict[e.id] = [deepcopy(e.position), deepcopy(e.get_flashlight_points())]


    def update(self, key, val):
        self.state_dict = deepcopy(val)
    
    def pos_changed(self, key, val):
        return equals(self.state_dict[key], val)
        
