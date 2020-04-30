#################################################################
#                                                               #
#                                                               #
#        The main Character class in the jaibreak game.         #
#        Extended to make enemy and main character classes      #
#                                                               #
#                                                               #
#################################################################



class Character:


    def __init__(self, position, step, image):
        self.position = position                 #Positioning Object
        self.step = step                         #How many pixels to move each step 
        self.image = image                       #Image to repr character
    
    # def valid_move()

    def step(self):
        d = self.position.get_direction()
        r, c = self.get_coords

        if d=='RIGHT':
            self.position.update_col(c+self.step)
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
        
        