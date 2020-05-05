import os


#Game base values
LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3 # Directions represented numerically
DIRECTIONS = [LEFT, UP, RIGHT, DOWN]


#Character related
STEP = 1
ENEMY_FLASHLIGHT_MULTIPLIER = 0.6
FLASHLIGHT_RANGE = 200

PROTAGONIST_IMAGE = './Images/Protagonist.png'
ENEMY_IMG = './Images/Enemy.png'


#Maps
MAP_OPTIONS = os.listdir(os.path.join('GameControl','Maps'))
for m in range(len(MAP_OPTIONS)):
    MAP_OPTIONS[m] = os.path.join('GameControl','Maps', MAP_OPTIONS[m])

COLORS = {
    'floor': (125, 125, 125),
    'wall': (80, 80, 80),
    'door':(255,0,0),
    'border': (30, 30, 30),
    'flashlight': (225, 245, 164),
}

MAP_KEYS = {
    '#': 'wall',
    '.': 'floor',
    '/': 'door'
    # 'w': 'obstacle'
}


#Game settings
RESOLUTION_OPTIONS = [(1280, 720), (1600, 900), (1920, 1080), (2560, 1440)]
FPS_OPTIONS = [30, 60, 120, 144]

