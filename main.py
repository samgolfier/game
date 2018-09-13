import pygame
import sys

import astronaut
import floor
import wall

s_width = 800
s_height = s_width

g_floor = pygame.sprite.Group()
g_wall = pygame.sprite.Group()

# for x in range(0, s_width, 32):
#     g_floor.add(floor.floor(x, s_height - 32))

# for x in range(300, 600, 32):
#     g_floor.add(floor.floor(x, s_height - 400))

floor.LoadFloor("floor_pattern.txt", g_floor, s_height)
wall.LoadWall("wall_p.txt", g_wall, s_height)

g_player = pygame.sprite.Group()
g_player.add(astronaut.astro())

#projectiles
g_projec = pygame.sprite.Group()

#Background
bg = pygame.image.load("background_img.png")



pygame.init()
screen = pygame.display.set_mode((s_width, s_height))

clock = pygame.time.Clock()

#floor.init()
#astronaut.init()

while True:
    #Window event, exits the game when x is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit(0)
    #Draws background as black
    #screen.fill((0,0,0))


    #g.clear(screen, screen.get_rect())
    

    #astronaut.draw(screen)
    # draw here

    #floor.draw(screen)

    g_floor.draw(screen)
    g_player.draw(screen)
    g_projec.draw(screen)

    g_player.update(g_floor, g_projec)
    g_projec.update()
    #Flips the display buffers
    pygame.display.flip()


    #Background
    screen.blit(bg, (0, 0))
    
    #Update sprites

    #floor.update()
    #floor_x, floor_y = floor.getPos()
    #astronaut.update(floor_y)

    #Tells program how many ticks per second
    clock.tick(30)
