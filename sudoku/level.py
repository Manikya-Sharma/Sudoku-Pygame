import pygame
from board import Board
from cell import Cell


class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        Board.initialize_cells()

    def get_input(self):
        if pygame.mouse.get_pressed()[0]:
            Board.detect_selection(pygame.mouse.get_pos())
        if pygame.key.get_pressed():
            for cell in Cell.existing_cells:
                if cell.is_selected:
                    l = pygame.key.get_pressed()
                    if l[pygame.K_1]:
                        cell.answer(1)
                    if l[pygame.K_2]:
                        cell.answer(2)
                    if l[pygame.K_3]:
                        cell.answer(3)
                    if l[pygame.K_4]:
                        cell.answer(4)
                    if l[pygame.K_5]:
                        cell.answer(5)
                    if l[pygame.K_6]:
                        cell.answer(6)
                    if l[pygame.K_7]:
                        cell.answer(7)
                    if l[pygame.K_8]:
                        cell.answer(8)
                    if l[pygame.K_9]:
                        cell.answer(9)
                    if l[pygame.K_BACKSPACE]:
                        cell.answer(0)

    def draw_objects(self):
        Board.draw_template(self.screen)
        Board.draw_cells(self.screen)

    def update(self):
        for cell in Cell.existing_cells:
            if cell.is_default:
                continue
            cell.check_correctness()
        Board.check_completeness()

    def play(self):
        self.get_input()
        self.draw_objects()
        self.update()
        return True   # TODO Return False on ending
