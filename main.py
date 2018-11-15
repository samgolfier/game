import pygame
import sys

import levelone
import menu

s_width = 800
s_height = s_width

pygame.init()
screen = pygame.display.set_mode((s_width, s_height))

#camera
level_h = 2*s_height
level_w = s_width

#camera = Camera(*to_be_implemented*, total_level_width, total_level_height)

clock = pygame.time.Clock()

#scene = levelone.Level(s_width, s_height)
scene = menu.Menu(s_width, s_height)

while True:
    
    #Window event, exits the game when x is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit(0)
    
    scene.draw(screen)
    scene.update()

    #Flips the display buffers
    pygame.display.flip()
    #Tells program how many ticks per second
    clock.tick(30)
