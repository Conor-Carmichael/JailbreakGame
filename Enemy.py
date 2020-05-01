#################################################################
#                                                               #
#                                                               #
#        The enemy class in the jaibreak game.                  #
#                                                               #
#                                                               #
#################################################################

from Character import Character
from global_values import *
import random


class Enemy(Character):

    def __init__(self, turn_probability, movement_probability, sight_range, positioning, step, image):
        # Pass character attributes up
        super().__init__(positioning, step, image)

        self.turn_probability = turn_probability         #Probability of turning at each tick
        self.movement_probability = movement_probability #Probability of taking a step at each tick

        if sight_range >= 2:
            self.sight_range = sight_range         
        else:
            raise ValueError('Sight Range value must be greater than one.')


    """ CLASS METHODS """

    def get_flashlight_points(self, width=1.0):
        # Width is scaling factore for 'flashlight' width. 1.0 makes a right isoceles.
        a = self.position.get_coords()
        b, c = None, None 
        direction = self.position.get_direction()

        if direction==0:
            b = (a[0]-self.sight_range, a[1]-self.sight_range*width)
            c = (a[0]-self.sight_range, a[1]+self.sight_range*width)

        elif direction==1:
            b = (a[0]-self.sight_range*width, a[1]-self.sight_range)
            c = (a[0]+self.sight_range*width, a[1]-self.sight_range)

        elif direction==2:
            b = (a[0]+self.sight_range, a[1]-self.sight_range*width)
            c = (a[0]+self.sight_range, a[1]+self.sight_range*width)
        elif direction==3:
            b = (a[0]-self.sight_range*width, a[1]+self.sight_range)
            c = (a[0]+self.sight_range*width, a[1]+self.sight_range)
        else:
            #Should never happen....
            raise Exception('Direction is unhinged!')
        
        return (a, b, c)


        # If I come back to this function, I have since updated Positioning back to x and y 
    # def get_fov(self):
    #     enemy_row, enemy_col, direction = self.position.get()
    #     fov = []

    #     horizontal = direction % 2 == 0 # Left = 0, Right = 2. If the sight cone needs to be computed horizontally
    #     cone_step_dir = 1 if direction > 1 else -1  # Right is 2, Down is 3. 

    #     upper_bound = (1 + self.sight_range)*cone_step_dir # Loop range
    #     # print(upper_bound)
    #     for vision_step in range(0, upper_bound, cone_step_dir): 
    #         if horizontal: # Iterating over columns (cone extends horizontally)
    #             # The current width of the triangle repr by this range, expands as it goes further from enemy
    #             cone_low = vision_step * -1
    #             cone_high = vision_step + 1

    #             vision_extension = [(enemy_row + r, enemy_col + vision_step) for r in range(cone_low, cone_high, cone_step_dir)]
    #             fov.extend(vision_extension)

    #         else:          # Iterating over rows   (cone extends vertically)
    #             cone_low = vision_step * -1
    #             cone_high = vision_step + 1

    #             vision_extension = [(vision_step+enemy_row , enemy_col+c) for c in range(cone_low, cone_high, cone_step_dir)]
    #             fov.extend(vision_extension)
        
    #     return fov

    def chance_turn(self):
        if random.random() < self.turn_probability:
            self.direction = random.random_choice(self.position.directions().remove(self.position.get_direction()))


    def move(self):
        if random.random() < self.movement_probability:
            super.move()

        

    # Super() Methods:
    def turn(self, arg):
        return super(Enemy, self).turn(arg)