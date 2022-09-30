import pygame
from settings import Constants


class Arrow:
    """To allow changing of values and also for back or play"""
    # Always a square
    def __init__(self, pos_x, pos_y, side,
                 direction, variable=None,
                 return_pressed = False):
        """Variable is the function to which it passes direction"""
        pygame.init()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.side = side
        self.direction = direction
        self.variable = variable
        self.return_pressed = return_pressed

        self.c = Constants()
        self.font = pygame.font.Font('freesansbold.ttf', side)
        if self.direction == +1:
            self.text = self.font.render(">", True, self.c.d["THEME"][2])
        elif self.direction == -1:
            self.text = self.font.render("<", True, self.c.d["THEME"][2])

    def draw(self, screen):
        # Draw square
        pygame.draw.rect(screen, self.c.d["THEME"][1],
        [self.pos_x, self.pos_y, self.side, self.side], 0)

        # Draw boundary
        pygame.draw.rect(screen, self.c.d["THEME"][2],
        [self.pos_x, self.pos_y, self.side, self.side], 1)

        # Blit text (i.e. arrow)
        screen.blit(self.text, (self.pos_x+self.side/2-self.text.get_width()/2,
         self.pos_y+self.side/2-self.text.get_height()/2))

    def detect_click(self, position):
        pos_x, pos_y = position
        if self.return_pressed:
            if (pos_x >= self.pos_x and pos_x <= self.pos_x+self.side)\
                and (pos_y >= self.pos_y and pos_y <= self.pos_y+self.side):
                return False
            else:
                return True
        elif self.variable:
            if (pos_x >= self.pos_x and pos_x <= self.pos_x+self.side)\
                and (pos_y >= self.pos_y and pos_y <= self.pos_y+self.side):
                self.variable(self.direction)



class SettingsScreen:
    """ Two settings can be modified:

    1. Theme
    2. Difficulty

    Must restart to allow changes to take place
    """
    def __init__(self, screen):
        # Initialization
        pygame.init()
        self.screen = screen
        self.c = Constants()

        # Font
        self.font_size = 25
        self.font = pygame.font.Font("freesansbold.ttf", self.font_size)
        self.padding = 40

        # Buttons
        self.button_size = 25

            # Back Button
        self.back_button = Arrow(self.padding,
        self.padding, self.button_size, -1, return_pressed =True)

        # Settings available
        self.theme_text = self.font.render("Theme", True, self.c.d["THEME"][2])
        self.theme_text_pos = (self.padding, 100)

        self.theme_back_button = Arrow(
            self.theme_text_pos[0]+self.theme_text.get_width()+self.padding,
            self.theme_text_pos[1], self.button_size, -1, self.theme_change)

    def draw(self):
        self.screen.fill(self.c.d["THEME"][0])
        self.back_button.draw(self.screen)

        self.screen.blit(self.theme_text, self.theme_text_pos)
        self.theme_back_button.draw(self.screen)

        pygame.display.update()


    def play(self):
        self.draw()

        # Buttons

        stay_here = True
        if pygame.mouse.get_pressed()[0]:

            # Back Button
            pos = pygame.mouse.get_pos()
            stay_here = self.back_button.detect_click(pos)

            # Theme related buttons
            self.theme_back_button.detect_click(pos)


        return True, stay_here   # means still initializing screen and open settings



    @staticmethod
    def theme_change(direction):
        pass
