#Game base values
LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3 # Directions represented numerically
DIRECTIONS = [LEFT, UP, RIGHT, DOWN]

#Character related
STEP = 2
ENEMY_FLASHLIGHT_MULTIPLIER = 0.6
FLASHLIGHT_RANGE = 200

PROTAGONIST_IMAGE = './Images/Protagonist.png'
ENEMY_IMG = './Images/Enemy.png'

#
COLORS = {
    'floor': (125, 125, 125),
    'obstacle': (80, 80, 80),
    'door':(255,0,0),
    'wall': (30, 30, 30),
    'flashlight': (225, 245, 164),
}

MAP_KEYS = {
    '#': 'wall',
    '.': 'floor',
    '/': 'door'
}

#Game settings
RESOLUTION_OPTIONS = [(1280, 720), (1600, 900), (1920, 1080), (2560, 1440)]
FPS_OPTIONS = [30, 60, 120, 144]