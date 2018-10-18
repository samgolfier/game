import pygame

class coll(pygame.sprite.Sprite):
    def __init__ (self):

        super().__init__()

    def update(self, *args):
        g_player = args[0]

        s = pygame.sprite.spritecollideany(self, g_player)
        if s != None:
            self.oncollision(s)

    def oncollision(self, sprite):
        pass

class coin(coll):
    def __init__ (self, x, y):

        super().__init__()

        self.image = pygame.image.load("assets/pacman-6.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def oncollision(self, sprite):
        sprite.score+= 100
        sprite.collected_coin = True
        self.kill()
    
