import pygame
import astronaut


floor = pygame.image.load("assets/floor.png")




def init():
    global x,y
    x, y = 0,768
def getPos():
    global x,y
    return x,y

def draw(screen):
    global x,y
    image = pygame.transform.scale(floor,(640,32))
    screen.blit(image, (x,y))

def update():
    pass


def LoadFloor(filename, group, height):
    with open(filename, 'r') as f:
        for line in f:
            l = line.split(",")
            x = (int(l[0])) * 32
            y = int(l[1]) * 32
            group.add(floor(x, (height+y) % height ))
            if x < 0:
                self.speed_x = self.speed_x * -1
                


class floor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        
        self.image = pygame.image.load("assets/floor.png")
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = x,y
    
