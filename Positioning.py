#################################################################
#                                                               #
#                                                               #
#        The Position class in the jaibreak game.               #
#        To stor a characters coordinates and direction         #
#                                                               #
#                                                               #
#################################################################

class Positioning:

    """ Holds an X, Y tuple, and direction """

    def __init__(self, x, y, d):
        self.x = X
        self.y = y 
        self.d = d if d in self.directions() else raise ValueError("Positioning.py: Provided invalid direction.{}".format(d))


    def get(self):
        return ((self.x, self.y), self.d)
    
    def get_coords(self):
        return self.x, self.y

    def get_direction(self):
        return self.d


    def directions(self):
        return ['LEFT', 'RIGHT', 'UP','DOWN']
    
    def print_pos(self):
        print("FACING: {} @ ({}, {})".format(self.d, self.x, self.y))