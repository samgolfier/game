import pygame
import levelone


#This is the menu that shows before the game starts
class Menu:
    def __init__(self, s_width, s_height):
        fontfile = pygame.font.match_font('arial')
        self.arial = pygame.font.Font(fontfile, 64)
        self.arial.set_bold(True)

        self.start_bordercol = (50,50,50)
        self.start_rect = None

        self.s_width = s_width
        self.s_height = s_height
        

    def draw(self, screen):
        (st_width, st_height) = screen.get_size()
        start = self.arial.render(("Start game") , False, (255,255,255))

        (w, h) = start.get_size()
        start_border = pygame.Surface((w+20, h+20))
        start_border.fill(self.start_bordercol)
        start_border.blit(start, (10, 10))

        x = (st_width / 2) - ((w+20)/2)
        y = (st_height / 2) - ((h+20)/2)

        self.start_rect = screen.blit(start_border, (x, y))


        #The 10 comes from dividing the 20 by 2
        

    def update(self):
        (mouse_x, mouse_y) = pygame.mouse.get_pos()

        (mouse_btn, btn2, btn3) = pygame.mouse.get_pressed()

        if self.start_rect.collidepoint(mouse_x, mouse_y):
            if mouse_btn:
                return levelone.Level(self.s_width, self.s_height)
            self.start_bordercol = (100,100,100)
        else:
            self.start_bordercol = (50,50,50)
        return self