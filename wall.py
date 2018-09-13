import pygame


wall = pygame.image.load("assets/wall.png")




def init():
    global x,y
    x, y = 0,768
def getPos():
    global x,y
    return x,y

def draw(screen):
    global x,y
    image = pygame.transform.scale(wall,(640,32))
    screen.blit(image, (x,y))

def update():
    pass


def LoadWall(filename, group, height):
    with open(filename, 'r') as f:
        for line in f:
            l = line.split(",")
            x = (int(l[0])) * 32
            y = int(l[1]) * 32
            group.add(wall(x, (height+y) % height ))


class wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        
        self.image = pygame.image.load("assets/wall.png")
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = x,y
    
