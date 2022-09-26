import pygame
from random import shuffle, choice
from cell import Cell
from settings import Constants


class Board:
    """
    *    METHOD OF PATHWAYS
        To get 3 blocks satisfying the block, row and column condition

    *     1.                    2.

    *     [•]   []   []         [•]   []   []

    *     []   [•]   []         []   []   [•]

    *     []   []   [•]         []   [•]   []
    """

    @staticmethod
    def get_final_three_blocks(ex_row_1, ex_row_2, ex_row_3, ex_row_4, ex_row_5, ex_row_6):
        row_7 = []
        row_8 = []
        row_9 = []
        array = [row_7, row_8, row_9]

        for i in range(9):
            ex_elements_in_column = Board.access_column([ex_row_1, ex_row_2,
                                    ex_row_3, ex_row_4, ex_row_5, ex_row_6], i)
            required_elements = Board.get_sub_list([1,2,3,4,5,6,7,8,9],ex_elements_in_column)

            shuffle(required_elements)
            # Will always satisfy column, row and block condition!
            Board.set_column_in_array(array, required_elements, i)

        return row_7, row_8, row_9


    @staticmethod
    def pathways_with_columns(lis, ex_row_1, ex_row_2, ex_row_3):
        return

    @staticmethod
    def pathways(lis):
        return

    # Miscellaneous Functions
    @staticmethod
    def get_sub_list(given_list, remove_list):
        for elem in remove_list:
            if elem in given_list:
                given_list.remove(elem)
        return given_list

    @staticmethod
    def access_column(array, column):
        lis = []
        for row in array:
            lis.append(row[column])
        return lis

    @staticmethod
    def set_column_in_array(existing_array, elements_list, column):
        # list is by default mutable type so call by reference
        i = 0
        for row in existing_array:
            try:
                row[column] = elements_list[i]
            except IndexError:
                row.insert(column, elements_list[i])
            i += 1

    @staticmethod
    def get_sudoku_array():
        STANDARD_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # Get first row
        row_1 = STANDARD_LIST
        shuffle(row_1)

        # Get the 3 blocks through pathways
        row_2, row_3 = Board.pathways(row_1)

        # Get the fourth row using randomization
        row_4 = []
        existing = []
        for i in range(9):
            required_list = Board.get_sub_list(
                STANDARD_LIST, [row_1[i], row_2[i], row_3[i]])
            new_elem = choice(required_list)
            while new_elem in existing:
                new_elem = choice(required_list)
            row_4.insert(i, new_elem)
            existing.append(new_elem)

        # Using pathways with column condition for row 5 and row 6
        row_5, row_6 = Board.pathways_with_columns(row_4, row_1, row_2, row_3)

        # Using method of remaining numbers to determine row 7,8 and 9
        row_7, row_8, row_9 = Board.get_final_3_blocks(
            row_1, row_2, row_3, row_4, row_5, row_6)

        final = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]
        return final

    @staticmethod
    def initialize_cells():
        # Number of defaults
        c = Constants()
        num_given = c.d["DIFFICULTY"]
        num_done = 0

        # ? # Allocating numbers
        final = Board.get_sudoku_array()
        # Creating the corresponding cells
        i = 1
        while i <= 9:
            j = 1
            while j <= 9:
                if num_done <= num_given:
                    rand = choice((0, 1))
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

    @staticmethod
    def draw_template(screen):
        c = Constants()
        major_box_side = c.get_cell_side()*3 + 2*c.d['PADDING']
        thickness = 1

        # Top 3
        pygame.draw.rect(screen, c.d["THEME"][7],
                         [c.d["SIDE_GAP"]-c.d["PADDING"]/2,
                          c.d["TOP_BOTTOM_GAP"]-c.d["PADDING"]/2,
                          major_box_side+c.d["PADDING"], major_box_side+c.d["PADDING"]], thickness)

        pygame.draw.rect(screen, c.d["THEME"][7],
                         [c.d["SIDE_GAP"]+major_box_side+c.d["PADDING"]/2,
                          c.d["TOP_BOTTOM_GAP"]-c.d["PADDING"]/2,
                          major_box_side+c.d["PADDING"], major_box_side+c.d["PADDING"]], thickness)

        pygame.draw.rect(screen, c.d["THEME"][7],
                         [c.d["SIDE_GAP"]+c.d["PADDING"]+2*major_box_side+c.d["PADDING"]/2,
                          c.d["TOP_BOTTOM_GAP"]-c.d["PADDING"]/2,
                          major_box_side+c.d["PADDING"], major_box_side+c.d["PADDING"]], thickness)

        # Middle 3
        pygame.draw.rect(screen, c.d["THEME"][7],
                         [c.d["SIDE_GAP"]-c.d["PADDING"]/2,
                          c.d["TOP_BOTTOM_GAP"] +
                          major_box_side+c.d["PADDING"]/2,
                          major_box_side+c.d["PADDING"], major_box_side+c.d["PADDING"]], thickness)

        pygame.draw.rect(screen, c.d["THEME"][7],
                         [c.d["SIDE_GAP"]+major_box_side+c.d["PADDING"]/2,
                          c.d["TOP_BOTTOM_GAP"] +
                          major_box_side+c.d["PADDING"]/2,
                          major_box_side+c.d["PADDING"], major_box_side+c.d["PADDING"]], thickness)

        pygame.draw.rect(screen, c.d["THEME"][7],
                         [c.d["SIDE_GAP"]+c.d["PADDING"]+2*major_box_side+c.d["PADDING"]/2,
                          c.d["TOP_BOTTOM_GAP"] +
                          major_box_side+c.d["PADDING"]/2,
                          major_box_side+c.d["PADDING"], major_box_side+c.d["PADDING"]], thickness)

        # Bottom 3
        pygame.draw.rect(screen, c.d["THEME"][7],
                         [c.d["SIDE_GAP"]-c.d["PADDING"]/2,
                          c.d["TOP_BOTTOM_GAP"]+c.d["PADDING"] +
                          2*major_box_side+c.d["PADDING"]/2,
                          major_box_side+c.d["PADDING"], major_box_side+c.d["PADDING"]], thickness)

        pygame.draw.rect(screen, c.d["THEME"][7],
                         [c.d["SIDE_GAP"]+major_box_side+c.d["PADDING"]/2,
                          c.d["TOP_BOTTOM_GAP"]+c.d["PADDING"] +
                          2*major_box_side+c.d["PADDING"]/2,
                          major_box_side+c.d["PADDING"], major_box_side+c.d["PADDING"]], thickness)

        pygame.draw.rect(screen, c.d["THEME"][7],
                         [c.d["SIDE_GAP"]+c.d["PADDING"]+2*major_box_side+c.d["PADDING"]/2,
                          c.d["TOP_BOTTOM_GAP"]+c.d["PADDING"] +
                          2*major_box_side+c.d["PADDING"]/2,
                          major_box_side+c.d["PADDING"], major_box_side+c.d["PADDING"]], thickness)

        # Complete Box
        pygame.draw.rect(screen, c.d["THEME"][7],
                         [c.d["SIDE_GAP"]-c.d["PADDING"]/2,
                          c.d["TOP_BOTTOM_GAP"]-c.d["PADDING"]/2,
                          3*major_box_side+3*c.d["PADDING"], 3*major_box_side+3*c.d["PADDING"]], thickness)

    @staticmethod
    def detect_selection(mouse_coords):
        m_x, m_y = mouse_coords
        c = Constants()
        for cell in Cell.existing_cells:
            c_x, c_y = (c.d["SIDE_GAP"]+(cell.column-1)*(cell.side+c.d["PADDING"]),
                        c.d["TOP_BOTTOM_GAP"]+(cell.row-1)*(cell.side+c.d["PADDING"]))

            if m_x >= c_x and m_x <= c_x+cell.side and m_y >= c_y and m_y <= c_y+cell.side:
                cell.is_selected = True
            else:
                cell.is_selected = False

    def check_completeness():
        for row in range(1, 10):
            row_cells = []
            for cell in Cell.existing_cells:
                if cell.row == row:
                    row_cells.append(cell)
            for cell in row_cells:
                if cell.number == 0 or cell.is_red:
                    # Something wrong or incomplete
                    valid = False
                    break
            else:
                valid = True
            if valid:
                Cell.make_green(row=row)
            else:
                Cell.remove_green(row=row)

        for column in range(1, 10):
            column_cells = []
            for cell in Cell.existing_cells:
                if cell.column == column:
                    column_cells.append(cell)
            for cell in column_cells:
                if cell.number == 0 or cell.is_red:
                    valid = False
                    break
            else:
                valid = True
            if valid:
                Cell.make_green(column=column)
            else:
                Cell.remove_green(column=column)
