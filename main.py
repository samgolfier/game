import pygame
import sys

from random import randint

import astronaut
import floor
import wall
import hazards
import collectables
import background_things as bg_stuff

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


#Score
pygame.font.init()
fontfile = pygame.font.match_font('arial')
arial = pygame.font.Font(fontfile, 32)
arial.set_bold(True)

flashtimer = 0


#projectiles
g_projec = pygame.sprite.Group()
g_projec.add(hazards.hazard())

#Background
bg = pygame.image.load("background_img.png")


#Coin
g_coin = pygame.sprite.Group()
for i in range(5):
    g_coin.add(collectables.coin(200,randint(400,600)))



#Background_things

g_bg = pygame.sprite.Group()


pygame.init()
screen = pygame.display.set_mode((s_width, s_height))

#camera
level_h = 2*s_height
level_w = s_width

#camera = Camera(*to_be_implemented*, total_level_width, total_level_height)

clock = pygame.time.Clock()

#floor.init()
#astronaut.init()

while True:
    #Window event, exits the game when x is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit(0)
    #Draws background as black
    #screen.fill((0,0,0))



    #camera
    
    #camera.update(player)
    


    #g.clear(screen, screen.get_rect())
    

    #astronaut.draw(screen)
    # draw here

    #floor.draw(screen)
    if g_player.sprites()[0].collected_coin:
        flashtimer += 30
        g_player.sprites()[0].collected_coin = False

    
    if flashtimer % 2 == 0:
        screen.blit(arial.render(("Score: %d" % g_player.sprites()[0].score) , False, (255,255,255)), (100, 10))
    else:
        screen.blit(arial.render(("Score: %d" % g_player.sprites()[0].score) , False, (255,0,0)), (100, 10))
    if flashtimer > 0:
        flashtimer = flashtimer - 1

    g_floor.draw(screen)
    g_player.draw(screen)
    g_projec.draw(screen)
    g_coin.draw(screen)
    g_bg.draw(screen)

    g_player.update(g_floor, g_projec)
    g_projec.update()

    g_coin.update(g_player)
    g_bg.update()
    #Flips the display buffers
    pygame.display.flip()


    #Background
    screen.blit(bg, (0, 0))
    
    n = randint(0,5*30) #15 seconds with 30 frames per second
    if n == 0:
        #g_coin.add(collectables.coin(200,randint(400,600)))
        g_bg.add(bg_stuff.ufo(0, randint(100,500), 5, 0))

    #Tells program how many ticks per second
    clock.tick(30)
