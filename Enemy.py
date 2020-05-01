#################################################################
#                                                               #
#                                                               #
#        The enemy class in the jaibreak game.                  #
#                                                               #
#                                                               #
#################################################################

from Character import Character
from GlobalValues import *
import random, pygame


class Enemy(Character):

    enemy_count = 0

    def __init__(self, flashlight_range, positioning, image):
        # Pass character attributes up
        super().__init__(positioning, image)

        self.flashlight_range = self.check_light_range(flashlight_range)

        self.turn_p = 0.05                #Probability of turning at each tick
        self.movement_p = 0.2            #Probability of taking a step at each tick
        self.turn_cooldown = 100

        Enemy.enemy_count += 1




    def get_flashlight_points(self, width=1.0):
        # Width is scaling factore for 'flashlight' width. 1.0 makes a right isoceles.
        a = self.get_loc()
        b, c = None, None 
        direction = self.get_dir()

        if direction==0:
            b = (a[0]-self.flashlight_range, a[1]-self.flashlight_range*width)
            c = (a[0]-self.flashlight_range, a[1]+self.flashlight_range*width)

        elif direction==1:
            b = (a[0]-self.flashlight_range*width, a[1]-self.flashlight_range)
            c = (a[0]+self.flashlight_range*width, a[1]-self.flashlight_range)

        elif direction==2:
            b = (a[0]+self.flashlight_range, a[1]-self.flashlight_range*width)
            c = (a[0]+self.flashlight_range, a[1]+self.flashlight_range*width)
        elif direction==3:
            b = (a[0]-self.flashlight_range*width, a[1]+self.flashlight_range)
            c = (a[0]+self.flashlight_range*width, a[1]+self.flashlight_range)
        else:
            #Should never happen....
            raise Exception('[Enemy.get_flashlight_points] Direction is unhinged!')
        
        return (a, b, c)


    def set_light_range(self, new_val):
        self.flashlight_range = self.check_light_range(new_val)

    def check_light_range(self, lr):
        if lr >= 2:
            return lr         
        else:
            raise ValueError('Flashlight Range value must be greater than one.')
            return

    def chance_turn(self):
        self.turn_cooldown = self.turn_cooldown-1 if self.turn_cooldown > 0 else self.turn_cooldown
        if self.turn_cooldown == 0 and random.random() < self.turn_p:

            self.position.update_direction( DIRECTIONS[random.randint(0,len(DIRECTIONS)-1) ] )
            self.turn_cooldown = 10
            return True
        else:
            return False


    def chance_move(self):
        if random.random() < self.movement_p:
            super(Enemy, self).move()
            return True
        else:
            return False
