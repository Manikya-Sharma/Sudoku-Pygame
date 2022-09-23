import pygame
from settings import Constants

class Start:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.c = Constants(True)

        # Start Button
        self.start_button_width = 150
        self.start_button_height = 50

        self.font = "freesansbold.ttf"
        self.font_size = 20

    def detect_click(self, position):
        pos_x, pos_y = position
        if (pos_x >= self.c.d["SCREEN_WIDTH"]/2 - self.start_button_width/2)\
            and (pos_x <= self.c.d["SCREEN_WIDTH"]/2 + self.start_button_width/2)\
                and (pos_y >= self.c.d["SCREEN_HEIGHT"])/2-self.start_button_height/2\
                    and (pos_y <= self.c.d["SCREEN_HEIGHT"]/2+self.start_button_height/2):
                    return "START"

    def draw_screen(self):
        # Start Button
        pygame.draw.rect(self.screen, self.c.d["THEME"][1],
        [self.c.d["SCREEN_HEIGHT"]/2-self.start_button_width/2,self.c.d["SCREEN_HEIGHT"]/2,
         self.start_button_width, self.start_button_height])

        # Start Text
        start_font = pygame.font.Font(self.font, self.font_size)
        start_text = start_font.render("START", True, self.c.d["THEME"][2])
        self.screen.blit(start_text,
        (self.c.d["SCREEN_WIDTH"]/2-self.start_button_width/2+start_text.get_width()/2,
        self.c.d["SCREEN_HEIGHT"]/2+self.start_button_height/2-start_text.get_height()/2))


    def play(self):
        self.draw_screen()
        if pygame.mouse.get_pressed()[0]:
            clicked = self.detect_click(pygame.mouse.get_pos())
        else:
            clicked = False
        if clicked == "START":
            print("Clicked")
            return False
        return True
