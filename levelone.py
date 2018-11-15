from random import randint

import pygame

import astronaut
import floor
import wall
import hazards
import collectables
import background_things as bg_stuff

class Level:
    def __init__(self, s_width, s_height):
        self.g_floor = pygame.sprite.Group()
        self.g_wall = pygame.sprite.Group()

        # for x in range(0, s_width, 32):
        #     self.g_floor.add(floor.floor(x, s_height - 32))

        # for x in range(300, 600, 32):
        #     self.g_floor.add(floor.floor(x, s_height - 400))

        floor.LoadFloor("floor_pattern.txt", self.g_floor, s_height)
        wall.LoadWall("wall_p.txt", self.g_wall, s_height)

        self.g_player = pygame.sprite.Group()
        self.g_player.add(astronaut.astro())


        #Score
        fontfile = pygame.font.match_font('arial')
        self.arial = pygame.font.Font(fontfile, 32)
        self.arial.set_bold(True)

        self.flashtimer = 0


        #projectiles
        self.g_projec = pygame.sprite.Group()
        self.g_projec.add(hazards.hazard(50, 50, 0, 0, 3))
        self.g_projec.add(hazards.hazard(50, 300, 0, 0, -3))
        self.g_projec.add(hazards.hazard(50, 500, 0, 0, 1))

        #Background
        self.bg = pygame.image.load("background_img.png")


        #Coin
        self.g_coin = pygame.sprite.Group()
        for i in range(5):
            self.g_coin.add(collectables.coin(200,randint(400,600)))



        #Background_things

        self.g_bg = pygame.sprite.Group()

    def draw(self, screen):
        #Background
        screen.blit(self.bg, (0, 0))

        if self.flashtimer % 2 == 0:
            score = self.arial.render(("Score: %d" % self.g_player.sprites()[0].score) , False, (255,255,255))
        else:
            score = self.arial.render(("Score: %d" % self.g_player.sprites()[0].score) , False, (255,0,0))
        
        (w, h) = score.get_size()
        score_border = pygame.Surface((w+20, h+20))
        score_border.fill((50,50,50))
        screen.blit(score_border, ((100-10),(10-10)))
        #The 10 comes from dividing the 20 by 2
        screen.blit(score, (100, 10))

        if self.flashtimer > 0:
            self.flashtimer = self.flashtimer - 1

        self.g_floor.draw(screen)
        self.g_player.draw(screen)
        self.g_projec.draw(screen)
        self.g_coin.draw(screen)
        self.g_bg.draw(screen)
        
    def update(self):
        if self.g_player.sprites()[0].collected_coin:
            self.flashtimer += 30
            self.g_player.sprites()[0].collected_coin = False

        

        self.g_player.update(self.g_floor, self.g_projec)
        self.g_projec.update(self.g_player)

        self.g_coin.update(self.g_player)
        self.g_bg.update()
        


        #Custom BG
        n = randint(0,2*30) #15 seconds with 30 frames per second
        if n == 0:
            #self.g_coin.add(collectables.coin(200,randint(400,600)))
            self.g_bg.add(bg_stuff.ufo(0, randint(100,500), 5, 0))

        return self