import pygame 

class bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =  pygame.image.load("assets/bullet0.png")
        self.rect = self.image.get_rect()