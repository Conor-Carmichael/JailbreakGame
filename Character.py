#################################################################
#                                                               #
#                                                               #
#        The main Character class in the jaibreak game.         #
#        Extended to make enemy and main character classes      #
#                                                               #
#                                                               #
#################################################################



class Character:


    def __init__(self, position, step, size):
        self.position = position                 #Positioning Object
        self.step = step                         #How many pixels to move each step 
        self.size = size                       #Image to repr character
    
    def valid_move(self, new_coords, map_bounds):
        new_x, new_y = new_coords
        x_lim, y_lim = map_bounds

        if new_x+self.size[0] >= x_lim or new_x < 0 or new_y+self.size[1] >= y_lim or new_y < 0:
            return False
        else:
            return True

    def step(self, map_bounds):
        d = self.position.get_direction()
        r, c = self.get_coords

        if d=='RIGHT':
            self.position.update_col(c+self.step) if self.valid_move((), map)
        elif d=='LEFT':
            self.position.update_col(c-self.step)

        elif d=='DOWN':
            self.position.update_row(r+self.step)
        elif d=='UP':
            self.position.update_row(r-self.step)
        

    def turn(self, new_dir):
        self.position.update_direction(new_dir)

    
    def get_pos(self):
        return self.position
        
        