#################################################################
#                                                               #
#                                                               #
#        The enemy class in the jaibreak game.                  #
#                                                               #
#                                                               #
#################################################################

from Character import Character



class Enemy(Character):

    def __init__(self, turn_probability, sight_range, position, step, image):
        super().__init__(position, step, image)

        self.turn_probability = turn_probability

        if sight_range >= 2:
            self.sight_range = sight_range         
        else:
            raise ValueError('Sight Range value must be greater than one.')



    def get_fov(self, coord_grid):
        # Returns an array of the pixels that are in the fov
        # https://keisan.casio.com/exec/system/1273849260
        # The FOV is a right isoceles triangle
        # The hypotenouse is 2*sight_range
        # The sides are SqRoot(2)*sight_range
        # This all doesn't seem necesary, just doing loops actually

        fov = []

        enemy_row, enemy_col = self.position.get_coords()
        row_limit, col_limit = len(coord_grid), len(coord_grid[0])

        direction = self.position.get_direction()
    
        horizontal = direction in ['LEFT', 'RIGHT'] # Working with cols or rows for fov

        # To set the direction we will loop on 
        # Doubles as step in range()
        range_multp = 1 if direction in ['RIGHT', 'DOWN'] else -1 
        

        if horizontal:
            # Enemy FOV extends horizontally

            # Upper bound for loop(), step will be -1 if left
            upper_bound = enemy_col + (1 + self.sight_range)*range_multp
            upper_bound = min(upper_bound, col_limit) if direction == 'RIGHT' else max(upper_bound, -1) # IF right, cant go beyond max width, if left cant go further left than 0
                                                                                                                

            for col in reversed(range(enemy_col, upper_bound, range_multp)):
                # Start with the biggest part of triangle fov
                # walk back, taking one off each side at a time
                # Will converge with enemy location

                vision_cone_width = abs(col - enemy_col)

                # Dont go out of bounds
                row_low = max(0, enemy_row-vision_cone_width)          #Checks to make sure the horizotal fov wont go above the viewport
                row_high = min(row_limit, enemy_row+vision_cone_width+1) #Checks to make sure horizontal fov wont go below viewport
                
                add_to_fov = coord_grid[row_low:row_high, col]
                fov.extend(add_to_fov)

        else:
            # Enemy FOV extends vertically

            # Loop upper bound for range(), if its up the step will be -1
            upper_bound = enemy_row + (1 + self.sight_range)*range_multp
            upper_bound = min(upper_bound, row_limit) if direction == 'DOWN' else max(-1, upper_bound) # will be uninclusive range, so -1 is ok

            for row in reversed(range(enemy_row, upper_bound, range_multp)):
                # Start with the biggest part of triangle fov
                # walk back, taking one off each side at a time
                # Will converge with enemy location

                vision_cone_width = abs(row - enemy_row)

                # Ensures not to index out of bounds on the coordinate grid.
                col_low = max(0, enemy_col-vision_cone_width)
                col_high = min(col_limit, enemy_col+1+vision_cone_width)
                
                add_to_fov = coord_grid[row,  col_low:col_high  ]
                fov.extend(add_to_fov)

        return fov