import pygame
from settings import Constants

class Game:
    def __init__(self):
        pygame.init()
        self.constants = Constants(True)
        self.screen = pygame.display.set_mode((self.constants.d['SCREEN_WIDTH'],
                        self.constants.d['SCREEN_HEIGHT']))
        self.running = True

    def end_game(self):
        self.running = False

    def play(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end_game()

if __name__ == "__main__":
    game = Game()
    game.play()
