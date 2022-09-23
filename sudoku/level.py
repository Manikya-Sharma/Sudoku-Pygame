import pygame
from board import Board

class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        Board.initialize_cells()

    def play(self):
        Board.draw_cells(self.screen)
        return True   # TODO Return False on ending
