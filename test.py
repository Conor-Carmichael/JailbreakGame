import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys, random
# import Character, Positioning, Enemy

from pygame.locals import *

print('eh')

pygame.init()
print('oh')
RESOLUTION = (1920, 1080)

DISPLAY_SURFACE = pygame.display.set_mode(RESOLUTION, 0, 32)
# pygame.set_caption('Jailbreak!')

# coord_grid = []
# for row in range(RESOLUTION[0]):
#     cg_row = []
#     for col in range(RESOLUTION[1]):
#         cg_row.append((row, col))
#     coord_grid.append(cg_row)

colors = {
    'k': (0,0,0),
    'w': (255,255,255)
}

DISPLAY_SURFACE.fill(colors['k'])

# enemy_start_pos = Positioning(100, 200, 'RIGHT')
# enemy = Enemy(0, 20, enemy_start_pos, 10, None)

# pix_obj = pygame.PixelArray(DISPLAY_SURFACE)



# for vision in enemy.get_fov(coord_grid):
#     pix_obj[vision[0]][vision[1]] = colors['w']


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()