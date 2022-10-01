import pickle
import pygame
from settings import Constants


class Arrow:
    """To allow changing of values and also for back or play"""
    # Always a square

    def __init__(self, pos_x, pos_y, side,
                 direction, variable=None,
                 return_pressed=False):
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
        with open("../data/user_settings.bin", 'rb') as file:
            self.data = pickle.load(file)

        # Font
        self.font_size = 25
        self.font = pygame.font.Font("freesansbold.ttf", self.font_size)
        self.padding = 40

        # Buttons
        self.button_size = 25

        # Back Button
        self.back_button = Arrow(self.padding,
                                 self.padding, self.button_size, -1, return_pressed=True)

        # Settings available

        # THEME
        self.theme_text = self.font.render("Theme", True, self.c.d["THEME"][2])
        self.theme_text_pos = (self.padding, 100)

        self.theme_back_button = Arrow(
            self.theme_text_pos[0]+self.theme_text.get_width()+self.padding,
            self.theme_text_pos[1], self.button_size, -1, self.theme_change)
        self.theme_options_text = self.font.render(
            ["LIGHT", "DARK"][self.data[0]], True, self.c.d["THEME"][2])
        self.theme_fwd_button = Arrow(
            self.theme_text_pos[0]+self.theme_text.get_width()+self.padding
            + self.button_size + self.padding
            + self.theme_options_text.get_width()+self.padding,
            self.theme_text_pos[1], self.button_size, +1, self.theme_change)

        self.theme_options_text_pos = (
            self.theme_text_pos[0]+self.theme_text.get_width() +
            self.padding+self.button_size+self.padding, 100)

        # DIFFICULTY
        self.difficulty_text = self.font.render(
            "Difficulty", True, self.c.d["THEME"][2])
        self.difficulty_text_pos = (self.padding, 200)

        self.difficulty_back_button = Arrow(
            self.difficulty_text_pos[0] +
            self.difficulty_text.get_width()+self.padding,
            self.difficulty_text_pos[1], self.button_size, -1, self.difficulty_change)
        self.difficulty_options_text = self.font.render(
            ["EASY", "MEDIUM", "DIFFICULT"][self.data[1]], True, self.c.d["THEME"][2])
        self.difficulty_fwd_button = Arrow(
            self.difficulty_text_pos[0] +
            self.difficulty_text.get_width()+30+self.padding
            + self.button_size + self.padding
            + self.difficulty_options_text.get_width()+self.padding,
            self.difficulty_text_pos[1], self.button_size, +1, self.difficulty_change)
        # +30 to accommodate the size of the word difficult
        self.difficulty_options_text_pos = (
            self.theme_text_pos[0]+self.difficulty_text.get_width() +
            self.padding+self.button_size+self.padding, 200)

        # Save Button
        self.save_button_width = 150
        self.save_button_height = 50
        self.save_button_x = 500
        self.save_button_y = 500

    def detect_save(self, position):
        pos_x, pos_y = position
        if ((pos_x >= self.save_button_x)
            and (pos_x <= self.save_button_x+self.save_button_width)
            and (pos_y >= self.save_button_y)
                and (pos_y <= self.save_button_y+self.save_button_height)):
            self.save_settings()

    def draw_save(self):
        # Save Button
        pygame.draw.rect(self.screen, self.c.d["THEME"][1],
                         [self.save_button_x, self.save_button_y,
                          self.save_button_width, self.save_button_height])

        # Save Text
        save_text = self.font.render("Save", True, self.c.d["THEME"][2])
        self.screen.blit(save_text, (self.save_button_x, self.save_button_y))

    def update_text(self):
        self.difficulty_options_text = self.font.render(
            ["EASY", "MEDIUM", "DIFFICULT"][self.data[1]], True, self.c.d["THEME"][2])
        self.theme_options_text = self.font.render(
            ["LIGHT", "DARK"][self.data[0]], True, self.c.d["THEME"][2])

    def draw(self):
        self.screen.fill(self.c.d["THEME"][0])
        self.back_button.draw(self.screen)

        self.screen.blit(self.theme_text, self.theme_text_pos)
        self.theme_back_button.draw(self.screen)
        self.screen.blit(self.theme_options_text, self.theme_options_text_pos)
        self.theme_fwd_button.draw(self.screen)

        self.screen.blit(self.difficulty_text, self.difficulty_text_pos)
        self.difficulty_back_button.draw(self.screen)
        self.screen.blit(self.difficulty_options_text,
                         self.difficulty_options_text_pos)
        self.difficulty_fwd_button.draw(self.screen)

        self.draw_save()
        pygame.display.update()

    def update(self):
        self.update_text()

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
            self.theme_fwd_button.detect_click(pos)

            # Difficulty related buttons
            self.difficulty_back_button.detect_click(pos)
            self.difficulty_fwd_button.detect_click(pos)

            # Save button
            self.detect_save(pos)

        self.update()

        return True, stay_here   # means still initializing screen and open settings

    def theme_change(self, direction):
        if self.data[0] == 0 and direction == +1:
            self.data[0] = 1
        elif self.data[0] == 1 and direction == -1:
            self.data[0] = 0

    def difficulty_change(self, direction):
        if self.data[1] > 0 and direction == -1:
            self.data[1] -= 1
        elif self.data[1] < 2 and direction == +1:
            self.data[1] += 1

    def save_settings(self):
        with open("../data/settings.bin", 'wb') as file:
            pickle.dump(self.data, file)
        print("HERE")
