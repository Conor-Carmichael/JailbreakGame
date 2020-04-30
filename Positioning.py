#################################################################
#                                                               #
#                                                               #
#        The Position class in the jaibreak game.               #
#        To stor a characters coordinates and direction         #
#                                                               #
#                                                               #
#################################################################

class Positioning:

    """ Holds an X, column tuple, and direction """

    def __init__(self, row, column, d):
        self.row = row
        self.column = column 
        if d in self.directions():
            self.d = d
        else: 
            raise ValueError("Positioning.py: Provided invalid direction.{}".format(d))


    def get(self):
        return ((self.row, self.column), self.d)
    
    def get_coords(self):
        return self.row, self.column

    def get_direction(self):
        return self.d


    def directions(self):
        return ['LEFT', 'RIGHT', 'UP','DOWN']
    
    def print_pos(self):
        print("FACING: {} @ ({}, {})".format(self.d, self.row, self.column))