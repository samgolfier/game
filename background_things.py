import pygame
from pygame.locals import *

class ufo(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):

        super().__init__()

        self.frames = pygame.image.load("assets/ufo.png")

        self.image = self.frames.subsurface(pygame.Rect(0,0,32,32)) # first frame of ufo
        self.frame = 0
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.speed_x = speed_x
        self.speed_y = speed_y

    def next_frame(self):
        self.frame += 1
        self.frame = self.frame % (3*5)

        # parent = self.image.get_parent()
        # (x, y) = parent.get_abs_offset()
        x = (self.frame // 5) * 32
        
        #x += self.image.get_rect().w
        # x = x % (self.image.get_rect().w)*3

        self.image = self.frames.subsurface(pygame.Rect(x,0,32,32))
        print(x)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        self.next_frame()