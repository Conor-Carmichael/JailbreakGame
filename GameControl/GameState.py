from copy import deepcopy
from Characters.Enemy import Enemy
from GlobalValues import *
from lib import *
import pygame

class GameState:

    def __init__(self, enemies, flashlights, protagonist, key): #protagonist, game_key):


        # All shallow copies for now since not doing dirty rectangles thing, no need to update
        self.protagonist = protagonist.rect
        self.enemies = [e.rect for e in enemies]
        self.flashlights = [f for f in flashlights] # Need to get points, so need whole sprite
        self.key = key


        # self.to_update = [] # List of rects to call update on 
        # self.character_locations, self.light_locations = {}, {}
        # self.character_locations[protagonist.id] = deepcopy(protagonist.get_loc())
        # for e in enemies:
        #     self.character_locations[e.id] = deepcopy(e.get_loc())
        #     self.light_locations[e.id+'-light'] = deepcopy(e.get_flashlight_points(ENEMY_FLASHLIGHT_MULTIPLIER))
        
        # self.protagonist = protagonist
        # self.enemies = enemies
        # Game state vars like timer, has_ley


    def blit_changes(self, dsp_srf):
        #Blit changes, 
        return 0

    def add_update(self, rect):
        self.to_update.append(rect)

    def clear_updates(self):
        self.to_update = []

    def get_updates(self):
        return self.to_update

    def get_character_loc(self, id):
        return self.character_locations[id]

    def get_enemy_light_loc(self, enemy_id):
        return self.light_locations[enemy_id+'-light']


    def update_loc(self, key, val):
        self.character_locations[key] = deepcopy(val)
    
    def update_light(self, key, val):
        self.light_locations[key+'-light'] = deepcopy(val)
 

    def protagonist_caught(self):
        # if they are too close to the enemy, or if they are in the light
        main_area = None

        # # Do not do calculations if protagonist is further than SIGHT_RANGE
        for fl, en in zip(self.flashlights, self.enemies):
            
            if distance(self.protagonist[0:2], en[0:2]) <= FLASHLIGHT_RANGE:
                corners = get_corner_coords((self.protagonist.x, self.protagonist.y), self.protagonist[2:4])
                print(corners)
                for corner in corners: # Check if corners are in sight
                    result, main_area = is_inside_triangle(fl.points, corner, main_area)
                    if result: # result None if not in, the sight triangel if inside. To check how its working.
                        print('Corner contact at ', corner, '. Sight Triangle Points: ', fl.points)
                        return True # (fl.points, corner) was used for deubggin
        
        return False #(None, None) #RESET TO FALSE AFTER DEBUGGING
        


    def key_collected(self):
        return