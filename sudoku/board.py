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
                                                         ex_row_3, ex_row_4,
                                                         ex_row_5, ex_row_6], i)
            required_elements = Board.get_sub_list(
                [1, 2, 3, 4, 5, 6, 7, 8, 9], ex_elements_in_column)

            shuffle(required_elements)
            # Will always satisfy column, row and block condition!
            Board.set_column_in_array(array, required_elements, i)

        return row_7, row_8, row_9

    @staticmethod
    def pathways_with_columns(lis, ex_row_1, ex_row_2, ex_row_3):
        # lis is the row 4
        d_row_5 = {}
        d_row_6 = {}
        block_1 = lis[:3]
        block_2 = lis[3:6]
        block_3 = lis[6:9]
        # TODO Was this needed?
        for i in range(3,9):
            col = Board.access_column([ex_row_1, ex_row_2, ex_row_3], i)
            if Board.get_num_common_elements(block_1, col) >= 3:
                if i//3 == 1:
                    for elem in block_1:
                        d_row_5[elem] = 3
                        d_row_6[elem] = 2
                    # Must go to block 3
                elif i//3 == 2:
                    for elem in block_1:
                        d_row_5[elem] = 2
                        d_row_6[elem] = 3
                    # Must go to block 2
        for i in range(9):
            if i in [3,4,5]:
                continue
            col = Board.access_column([ex_row_1, ex_row_2, ex_row_3], i)
            if Board.get_num_common_elements(block_2, col) >= 3:
                if i//3 == 0:
                    for elem in block_2:
                        d_row_5[elem] = 3
                        d_row_6[elem] = 1
                    # Must go to block 3
                elif i//3 == 2:
                    for elem in block_2:
                        d_row_5[elem] = 1
                        d_row_6[elem] = 3
                    # Must go to block 1
        for i in range(6):
            col = Board.access_column([ex_row_1, ex_row_2, ex_row_3], i)
            if Board.get_num_common_elements(block_3, col) >= 3:
                if i//3 == 0:
                    for elem in block_3:
                        d_row_5[elem] = 2
                        d_row_6[elem] = 1
                    # Must go to block 2
                elif i//3 == 1:
                    for elem in block_3:
                        d_row_5[elem] = 1
                        d_row_6[elem] = 2
                    # Must go to block 1
        

    @staticmethod
    def pathways(lis):
        row_2 = []
        row_3 = []
        block_21 = []
        block_22 = []
        block_23 = []
        block_31 = []
        block_32 = []
        block_33 = []
        for i in range(len(lis)):
            existing_block = (i//3)+1
            # IN BLOCK 1
            if existing_block == 1:
                next_block = choice((2, 3))
                if next_block == 2:
                    if len(block_22) < 3 and len(block_33) < 3:
                        next_block = 2
                    else:
                        next_block = 3
                if next_block == 3:
                    if len(block_23) < 3 and len(block_32) < 3:
                        next_block = 3
                    else:
                        next_block = 2
                # Now add to 3rd row
                if next_block == 2:
                    next_to_next_block = 3
                elif next_block == 3:
                    next_to_next_block = 2
            # IN BLOCK 2
            elif existing_block == 2:
                next_block = choice((1, 3))
                if next_block == 1:
                    if len(block_21) < 3 and len(block_33) < 3:
                        next_block = 1
                    else:
                        next_block = 3
                if next_block == 3:
                    if len(block_23) < 3:
                        next_block = 3
                    else:
                        next_block = 1
                # Now add to 3rd row
                if next_block == 1:
                    next_to_next_block = 3
                elif next_block == 3:
                    next_to_next_block = 1
            # IN BLOCK 3
            elif existing_block == 3:
                next_block = choice((1, 2))
                if next_block == 1:
                    if len(block_21) < 3 and len(block_32) < 3:
                        next_block = 1
                    else:
                        next_block = 2
                if next_block == 2:
                    if len(block_22) < 3 and len(block_31) < 3:
                        next_block = 2
                    else:
                        next_block = 1
                # Now add to 3rd row
                if next_block == 2:
                    next_to_next_block = 1
                elif next_block == 1:
                    next_to_next_block = 2

            if next_block == 1:
                block_21.append(lis[i])
            elif next_block == 2:
                block_22.append(lis[i])
            elif next_block == 3:
                block_23.append(lis[i])

            if next_to_next_block == 1:
                block_31.append(lis[i])
            elif next_to_next_block == 2:
                block_32.append(lis[i])
            elif next_to_next_block == 3:
                block_33.append(lis[i])

        shuffle(block_21)
        shuffle(block_22)
        shuffle(block_23)
        row_2.extend(block_21)
        row_2.extend(block_22)
        row_2.extend(block_23)

        shuffle(block_31)
        shuffle(block_32)
        shuffle(block_33)
        row_3.extend(block_31)
        row_3.extend(block_32)
        row_3.extend(block_33)

        return row_2, row_3

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
    def get_num_common_elements(lis1, lis2):
        count = 0
        for elem in lis1:
            if elem in lis2:
                count += 1
        return count

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
        row_1 = STANDARD_LIST.copy()
        shuffle(row_1)
        print("GOT ROW1")

        # Get the 3 blocks through pathways
        row_2, row_3 = Board.pathways(row_1)
        print("GOT ROW 2 AND 3")
        # Get the fourth row using randomization
        row_4 = []
        existing = []
        for i in range(9):
            required_list = Board.get_sub_list(
                STANDARD_LIST.copy(), [row_1[i], row_2[i], row_3[i]])
            new_elem = choice(required_list)
            while new_elem in existing:
                new_elem = choice(required_list)
            row_4.insert(i, new_elem)
            existing.append(new_elem)

        print("GOT ROW 4")
        # Using pathways with column condition for row 5 and row 6
        row_5, row_6 = Board.pathways_with_columns(row_4, row_1, row_2, row_3)
        # row_5, row_6 = [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]

        # Using method of remaining numbers to determine row 7,8 and 9
        row_7, row_8, row_9 = Board.get_final_three_blocks(
            row_1, row_2, row_3, row_4, row_5, row_6)

        print("GOT ROW 7,8,9")
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
