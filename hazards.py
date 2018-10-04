import pygame
from pygame.locals import *

class hazard(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("assets/hazard.png")  #Change this to a different sprite later
        self.rect = self.image.get_rect()
