#################################################################
#                                                               #
#                                                               #
#        The Position class in the jaibreak game.               #
#        To stor a characters coordinates and direction         #
#                                                               #
#                                                               #
#################################################################
from global_values import *


class Positioning:

    """       Holds X, Y, and direction        """

    def __init__(self, x=0, y=0, d=0):
        self.x = x
        self.y = y 
        if d in range(0, 4):
            self.d = d
        else: 
            raise ValueError("Positioning.py: Provided invalid direction. {}".format(d))


    #Get state
    def get(self):
        return (self.x, self.y, self.d)
    
    def get_coords(self):
        return (self.x, self.y)

    def get_direction(self):
        return self.d


    #Update
    def update_x(self, xn):
        self.x = xn
    
    def update_y(self, yn):
        self.y = yn

    def update_direction(self, dn):
        self.d = dn


    #General
    
    def direction_string(self):
        # I repr direction as int for space, to get value index into this arr
        return ['LEFT','UP','RIGHT','DOWN']

    
    def print_pos(self):
        print("FACING: {} @ ({}, {})".format(self.direction_string(self.d), self.row, self.column))