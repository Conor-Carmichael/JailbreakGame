import os


#Game base values
LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3 # Directions represented numerically
DIRECTIONS = [LEFT, UP, RIGHT, DOWN]


#Character related
STEP = 2
ENEMY_FLASHLIGHT_MULTIPLIER = 0.6
FLASHLIGHT_RANGE = 200

PROTAGONIST_IMAGE = './Images/Protagonist.png'
ENEMY_IMG = './Images/Enemy.png'


#Maps
MAP_IMAGES_PATH = os.path.join('GameControl','Maps', 'images')
MAP_INFO_PATH = os.path.join('GameControl','Maps', 'info')
MAP_FILE_NAMES = os.listdir(MAP_IMAGES_PATH) # info and image directories need to share file name



COLORS = {
    'floor': (120, 100, 55),
    'wall': (0, 0, 0),
    'door':(255,0,0),
    'border': (30, 30, 30),
    'flashlight': (225, 245, 164),
}



#Game settings
RESOLUTION_OPTIONS = [(1280, 720), (1600, 900), (1920, 1080), (2560, 1440)]
FPS_OPTIONS = [30, 60, 120, 144]

