import pygame
from pygame.locals import *

class hazard(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y, d_theta):

        super().__init__()

        self.graphics = pygame.image.load("assets/hazard.png")  #Change this to a different sprite later
        self.image = self.graphics
        self.rect = self.image.get_rect()

        self.d_theta = d_theta
        self.theta = 0

        self.rect.x = self.x = x
        self.rect.y = self.y = y

        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self, *args):
        g_player = args[0]

        s = pygame.sprite.spritecollideany(self, g_player)
        if s != None:
            self.oncollision(s)

        self.y += self.speed_y
        self.x += self.speed_x

        self.theta += self.d_theta
        self.image = pygame.transform.rotate(self.graphics, self.theta)

        self.rect.x = self.x - self.image.get_rect().width/2
        self.rect.y = self.y - self.image.get_rect().height/2
    
    def oncollision(self, sprite):
        sprite.hp-= 50
        self.kill()
        if sprite.hp <= 0:
            sprite.kill()