#################################################################
#                                                               #
#                                                               #
#        The enemy class in the jaibreak game.                  #
#                                                               #
#                                                               #
#################################################################

import Character.py



class Enemy(Character):

    def __init__(self, turn_probability, sight_range, *args, **kw):
        super().__init__( *args, **kw)

        self.turn_probability = turn_probability
        self.sight_range = sight_range


    # I tested this in colab notebook. 
    # NEED TO SET UP BOUNDS
    def calculate_fov(self, coord_grid):
        # Returns an array of the pixels that are in the fov
        # https://keisan.casio.com/exec/system/1273849260
        # The FOV is a right isoceles triangle
        # The hypotenouse is 2*sight_range
        # The sides are SqRoot(2)*sight_range
        # This all doesn't seem necesary, just doing loops actually

        fov = []

        x, y = self.position.get_coords()[0], self.position.get_coords()[1]
        x_limit, y_limit = len(coord_grid), len(coord_grid[0])
        direction = self.position.get_direction()
    
        horizontal = direction in ['LEFT', 'RIGHT'] # Working with cols or rows for fov

        # To set the direction we will loop on 
        # Doubles as step in range()
        range_multp = 1 if direction in ['RIGHT', 'DOWN'] else -1 
        
        vision_cone_width = self.sight_range # Will be decremented to get thinning cone


        if horizontal:
            # Enemy FOV extends horizontally

            # Upper bound for loop(), step will be -1 if left
            upper_bound = y + (1 + self.sight_range)*range_multp
            upper_bound = min(upper_bound, y_limit) # CACCOUNT FO RLEFT
            for col in reversed(range(y, upper_bound, range_multp)):
                # Start with the biggest part of triangle fov
                # walk back, taking one off each side at a time
                # Will converge with enemy location

                # Dont go out of bounds
                x_low = max(0, x-vision_cone_width) 
                x_high = min(x_limit, x+vision_cone_width+1)

                add_to_fov = coord_grid[ : , col]
                fov.extend(add_to_fov)
                vision_cone_width -= 1

        else:
            # Enemy FOV extends vertically

            # Loop upper bound for range(), if its up the step will be -1
            upper_bound = x + (1 + self.sight_range)*range_multp
            upper_bound = min(upper_bound, x_limit)
            for row in reversed(range(x, upper_bound, range_multp)):
                # Start with the biggest part of triangle fov
                # walk back, taking one off each side at a time
                # Will converge with enemy location
                add_to_fov = coord_grid[row, y-vision_cone_width : y+1+vision_cone_width ]
                fov.extend(add_to_fov)
                vision_cone_width -= 1

        return fov