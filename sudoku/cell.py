import pygame
from settings import Constants

class Cell:
    existing_cells = []
    font = "freesansbold.ttf"
    font_size = 20

    def __init__(self, row, column, default_number, is_default, is_answered = False):
        self.row = row
        self.column = column
        self.default_number = default_number
        self.is_default = is_default
        if self.is_default:
            self.number = self.default_number
        else:
            self.number = 0  # Impossible number
        self.c = Constants()
        self.side = self.c.get_cell_side()
        self.is_answered = is_answered
        Cell.existing_cells.append(self)

    def draw(self, screen):
        pygame.draw.rect(screen, self.c.d["THEME"][3],
        [self.c.d["SIDE_GAP"]+(self.column-1)*(self.side+self.c.d["PADDING"]),
        self.c.d["TOP_BOTTOM_GAP"]+(self.row-1)*(self.side+self.c.d["PADDING"]), self.side, self.side])

        font = pygame.font.Font(self.font, self.font_size)
        if self.is_default:
            text = font.render(str(self.default_number), True, self.c.d["THEME"][5])
        elif self.is_answered and not self.number == 0:
            text = font.render(str(self.number), True, self.c.d["THEME"][6])
        else:
            text = None
        if text is not None:
            screen.blit(text,
            (self.c.d["SIDE_GAP"]+(self.column-1)*(self.side+self.c.d["PADDING"])\
                +self.side/2-text.get_width()/2,
            self.c.d["TOP_BOTTOM_GAP"]+(self.row-1)*(self.side+self.c.d["PADDING"])\
                +self.side/2-text.get_height()/2))
