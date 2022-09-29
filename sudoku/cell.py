import pygame
from settings import Constants


class Cell:
    existing_cells = []
    font = "freesansbold.ttf"
    font_size = 20
    green_rows = []
    green_columns = []

    def __init__(self, row, column, default_number, is_default, is_answered=False, is_selected=False):
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
        self.is_selected = is_selected
        self.is_red = False   # For error numbers
        self.is_green = False  # For completed rows/columns
        Cell.existing_cells.append(self)

    def draw(self, screen):
        # Cell BG
        if self.is_red:
            color = (255, 0, 0)
        elif self.is_green:
            color = (0, 255, 0)
        else:
            color = self.c.d["THEME"][3]

        pygame.draw.rect(screen, color,
                         [self.c.d["SIDE_GAP"]+(self.column-1)*(self.side+self.c.d["PADDING"]),
                          self.c.d["TOP_BOTTOM_GAP"] +
                          (self.row-1)*(self.side+self.c.d["PADDING"]),
                          self.side, self.side])

        # Font
        font = pygame.font.Font(self.font, self.font_size)
        if self.is_default:
            text = font.render(str(self.default_number),
                               True, self.c.d["THEME"][5])
        elif self.is_answered and not self.number == 0:
            text = font.render(str(self.number), True, self.c.d["THEME"][6])
        else:
            text = None
        if text is not None:
            screen.blit(text,
                        (self.c.d["SIDE_GAP"]+(self.column-1)*(self.side+self.c.d["PADDING"])
                         + self.side/2-text.get_width()/2,
                         self.c.d["TOP_BOTTOM_GAP"] +
                         (self.row-1)*(self.side+self.c.d["PADDING"])
                            + self.side/2-text.get_height()/2))

        # Selection Rectangle
        if self.is_selected:
            pygame.draw.rect(screen, self.c.d["THEME"][8],
                             [self.c.d["SIDE_GAP"]+(self.column-1)*(self.side+self.c.d["PADDING"]),
                              self.c.d["TOP_BOTTOM_GAP"] +
                              (self.row-1)*(self.side+self.c.d["PADDING"]),
                              self.side, self.side], 2)

    def answer(self, number):
        if not self.is_default and number != 0:
            self.is_answered = True
            self.number = number
        elif number == 0:
            self.is_answered = False
            self.number = 0

    def check_correctness(self):
        for cell in Cell.existing_cells:
            if cell == self or cell.number == 0:
                continue
            if (cell.row == self.row or cell.column == self.column) and (cell.number == self.number):
                self.is_red = True
                break
        else:
            self.is_red = False

    @classmethod
    def make_green(cls, row=None, column=None):
        if row is None and column is None:
            return
        if row is not None:
            Cell.green_rows.append(row)
            for cell in cls.existing_cells:
                if cell.row == row:
                    cell.is_green = True
            return
        if column is not None:
            Cell.green_columns.append(column)
            for cell in cls.existing_cells:
                if cell.column == column:
                    cell.is_green = True
            return

    @classmethod
    def remove_green(cls, row=None, column=None):
        if not row and not column:
            return
        if row:
            for cell in cls.existing_cells:
                if cell.row == row and cell.column not in Cell.green_columns:
                    cell.is_green = False
                    try:
                        Cell.green_rows.remove(cell.row)
                    except ValueError:
                        pass         # Was not in green
            return
        if column:
            for cell in cls.existing_cells:
                if cell.column == column and cell.row not in Cell.green_rows:
                    cell.is_green = False
                    try:
                        Cell.green_columns.remove(cell.column)
                    except ValueError:
                        pass
            return
