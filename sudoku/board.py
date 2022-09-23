import pygame
from random import shuffle, choice
from cell import Cell
from settings import Constants

class Board:
    @staticmethod
    def initialize_cells():
        # Number of defaults
        c = Constants()
        num_given = c.d["DIFFICULTY"]
        num_done = 0

        # Allocating numbers
        final = []
        for j in range(9):   # Each row
            valid = False
            while not valid:
                column = [1,2,3,4,5,6,7,8,9]
                shuffle(column)
                for existing in final:
                    i = 0
                    while i<9:
                        if existing[i] == column[i]:
                            valid = False
                            break
                        i+=1
                    else:
                        valid = True
                final.append(column)
        i = 1
        while i <= 9:
            j = 1
            while j <= 9:
                if num_done <= num_given:
                    rand = choice((0,1))
                    if rand:
                        Cell(i, j, final[i-1][j-1], True)
                        num_done += 1
                        j += 1
                        continue
                Cell(i, j, final[i-1][j-1], False)
                j += 1
            i += 1

    @staticmethod
    def draw_cells(screen):
        for cell in Cell.existing_cells:
            cell.draw(screen)
