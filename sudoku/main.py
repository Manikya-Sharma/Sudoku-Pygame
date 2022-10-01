
# TODO: Make end screen, add option to show answer after lose, also settings for making defaults, better dark theme colors choice...

import pygame
from settings import Constants
from start_screen import Start
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("SUDOKU")
        self.c = Constants(True)
        self.screen = pygame.display.set_mode((self.c.d['SCREEN_WIDTH'],
                                               self.c.d['SCREEN_HEIGHT']))
        self.running = True
        self.initialize = True
        self.start = Start()
        self.level = Level()

    def end_game(self):
        self.running = False

    def play(self):
        while self.running:
            self.screen.fill(self.c.d['THEME'][0])

            if self.initialize:
                self.initialize = self.start.play()
            else:
                self.running = self.level.play()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end_game()
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    # while True:
        # try:
    game = Game()
    game.play()
        # except:
        #     print("ERROR")  #!For testing
        # else:
        #     break
