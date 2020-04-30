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
        self.sight_range = sight_range           #How far the enemy can see the player
        self.step = step                         #How many pixels to move each step 
        self.image = image                       #Image to repr character
    
    def move(self):
        return

    def turn(self, new_dir):
        return

    
        
        