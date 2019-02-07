import pygame
import levelone


#This is the screen that shows when the player dies
class Endscreen:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/endscreen.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image,(0,0))

    def update(self, *args):
        return self