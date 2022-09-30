# Added a new file to prevent congestion in Board.py
import pygame
from settings import Constants


class Loading:
    def __init__(self, screen, num_parts):
        # Initialize
        pygame.init()
        self.screen = screen
        self.c = Constants()

        # For loading bar
        self.num_parts = num_parts
        self.is_loaded = 0
        self.bar_width = 200
        self.bar_height = 10

        # For loading text
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.text = self.font.render("LOADING", True, self.c.d["THEME"][2])

    def draw_and_update(self):
        # Draw Background
        self.screen.fill(self.c.d["THEME"][0])

        # Blit Text
        self.screen.blit(self.text,
        (self.c.d["SCREEN_WIDTH"]/2-self.text.get_width()/2,
        self.c.d["SCREEN_HEIGHT"]/2-self.text.get_height()))

        # Bar Background
        pygame.draw.rect(
            self.screen, self.c.d["THEME"][1],
            [self.c.d["SCREEN_WIDTH"]/2-self.bar_width/2,
            self.c.d["SCREEN_HEIGHT"]/2+self.text.get_height(),
            self.bar_width, self.bar_height], 2)

        # Bar filling
        pygame.draw.rect(
            self.screen, self.c.d["THEME"][1],
            [self.c.d["SCREEN_WIDTH"]/2-self.bar_width/2,
            self.c.d["SCREEN_HEIGHT"]/2+self.text.get_height(),
            self.bar_width*(self.is_loaded/self.num_parts), self.bar_height], 0)

        pygame.display.update()

    def increment_loading(self):
        if self.is_loaded < self.num_parts:
            self.is_loaded += 1

    def set_zero(self):
        self.is_loaded = 0
