import pygame
from settings import Constants
from settings_screen import SettingsScreen

class Start:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.c = Constants(True)

        # Buttons
        self.start_button_width = 150
        self.start_button_height = 50

        self.font = "freesansbold.ttf"
        self.font_size = 20
        self.padding = 40

        # Sudoku Font
        self.sudoku_font = "freesansbold.ttf"
        self.sudoku_font_size = 120

        # Settings Screen
        self.settings_screen = SettingsScreen(self.screen)
        self.open_settings = False

    def detect_click(self, position):
        pos_x, pos_y = position
        if (pos_x >= self.c.d["SCREEN_WIDTH"]/2 - self.start_button_width/2)\
            and (pos_x <= self.c.d["SCREEN_WIDTH"]/2 + self.start_button_width/2)\
                and (pos_y >= self.c.d["SCREEN_HEIGHT"])/2-self.start_button_height/2\
        and (pos_y <= self.c.d["SCREEN_HEIGHT"]/2+self.start_button_height/2):
            return "START"

        if (pos_x >= self.c.d["SCREEN_WIDTH"]/2 - self.start_button_width/2)\
            and (pos_x <= self.c.d["SCREEN_WIDTH"]/2 + self.start_button_width/2)\
                and (pos_y >= self.c.d["SCREEN_HEIGHT"]/2+self.start_button_height/2\
                    + self.padding)\
        and (pos_y <= self.c.d["SCREEN_HEIGHT"]/2+self.start_button_height/2\
            +self.padding+self.start_button_height):
            return "SETTINGS"

    def draw_screen(self):
        # Sudoku Text
        sudoku_font = pygame.font.Font(self.sudoku_font, self.sudoku_font_size)
        sudoku_text = sudoku_font.render("SUDOKU", True, self.c.d["THEME"][2])
        self.screen.blit(sudoku_text,
                         (self.c.d["SCREEN_WIDTH"]/2-sudoku_text.get_width()/2, 100))

        # Start Button
        pygame.draw.rect(self.screen, self.c.d["THEME"][1],
                         [self.c.d["SCREEN_WIDTH"]/2-self.start_button_width/2,
                          self.c.d["SCREEN_HEIGHT"]/2 -
                          self.start_button_height/2,
                          self.start_button_width, self.start_button_height])

        # Start Text
        start_font = pygame.font.Font(self.font, self.font_size)
        start_text = start_font.render("START", True, self.c.d["THEME"][2])
        self.screen.blit(start_text,
                         (self.c.d["SCREEN_WIDTH"]/2-start_text.get_width()/2,
                          self.c.d["SCREEN_HEIGHT"]/2-start_text.get_height()/2))

        # Settings Button
        pygame.draw.rect(self.screen, self.c.d["THEME"][1],
                         [self.c.d["SCREEN_WIDTH"]/2-self.start_button_width/2,
                          self.c.d["SCREEN_HEIGHT"]/2 +
                          self.start_button_height/2+self.padding,
                          self.start_button_width, self.start_button_height])

        # Settings Text
        start_font = pygame.font.Font(self.font, self.font_size)
        start_text = start_font.render("SETTINGS", True, self.c.d["THEME"][2])
        self.screen.blit(start_text,
                         (self.c.d["SCREEN_WIDTH"]/2-start_text.get_width()/2,
                          self.c.d["SCREEN_HEIGHT"]/2+self.start_button_height/2\
                            +self.padding+start_text.get_height()/2))

    def play(self):
        if not self.open_settings:
            self.draw_screen()
            if pygame.mouse.get_pressed()[0]:
                clicked = self.detect_click(pygame.mouse.get_pos())
            else:
                clicked = False

            if clicked == "START":
                return False
            elif clicked == "SETTINGS":
                self.open_settings = True
                return True
        else:
            initialize, self.open_settings = self.settings_screen.play()
            return initialize
        return True
