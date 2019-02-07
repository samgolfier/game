import pygame
from pygame.locals import *
import bullet
import time

class astro(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.image = pygame.image.load("assets/astro0.png")
        self.rect = self.image.get_rect()
        
        #score value
        self.score = 0

        self.collected_coin = False

        self.rect.x, self.rect.y = 0, 0
        self.speed_x = 2
        self.speed_y = 0
        self.hp = 100

    def update(self, *args):
        if self.hp <= 0:
            self.kill()
            return

        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        self.speed_y += 0.2

        g_floor = args[0]
        g_projec = args[1]

        s = pygame.sprite.spritecollideany(self, g_floor)
        if s != None and self.speed_y > 0:
            self.speed_y *= -.7

        pygame.key.set_repeat(True)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            g_projec.add(bullet.bullet())
        elif keys[pygame.K_LEFT]:
            self.speed_x = -abs(self.speed_x)
        elif keys[pygame.K_RIGHT]:
            self.speed_x = abs(self.speed_x)

            
