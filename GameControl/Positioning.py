#################################################################
#                                                               #
#                                                               #
#        The Position class in the jaibreak game.               #
#        To stor a characters coordinates and direction         #
#                                                               #
#                                                               #
#################################################################
from GlobalValues import *
import numpy as np


class Positioning:

    """   Holds X, Y, and direction[0,1,2,3 : l, u, r, d]    """

    def __init__(self, x = None, y = None, d = None):
        self.x = x if x is not None else 0
        self.y = y if y is not None else 0
        self.d = self.direction_valid(d)


    #Get
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

    def set_rand(self, mx, my, var):
        x, y = self.generate_in_norm_dist(mx, my, var)
        self.update_x(x)
        self.update_y(y)


    #Functionality
    def equals(a, b):
        return a.x == b.x and a.y == b.y and a.d == b.d

    def generate_in_norm_dist(self, mean_x=200, mean_y=200, variance=50):
        x = np.random.normal(mean_x, variance)
        y = np.random.normal(mean_y, variance)
        return (int(x), int(y))

    def direction_valid(self, d):
        if d in range(0, 4):
            return d
        elif not d:
            return LEFT
        else: 
            raise ValueError("Positioning.py: Provided invalid direction. {}".format(d))

    def directions(self):
        return [0,1,2,3]

    def direction_string(self, d):
        # I repr direction as int, to get value index into this arr
        return ['LEFT','UP','RIGHT','DOWN'][d]

    def print_pos(self):
        print("FACING: {} @ ({}, {})".format(self.direction_string(self.d), self.x, self.y))