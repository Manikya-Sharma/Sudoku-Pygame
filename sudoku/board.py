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
        vertical_array = []  # To check the row condition

        for i in range(9):
            ex_elements_in_column = Board.access_column([ex_row_1, ex_row_2,
                                                         ex_row_3, ex_row_4,
                                                         ex_row_5, ex_row_6], i)
            required_elements = Board.get_sub_list(
                [1, 2, 3, 4, 5, 6, 7, 8, 9], ex_elements_in_column)
            # Will always satisfy column and block condition

            shuffle(required_elements)
            # Could have used a better approach than looping the same shuffle,
            # but since maximum permutations in the last 3 rows is 6, so it
            # will not affect efficiency too  much.

            for _ in range(3):
                for j in range(3):
                    if required_elements[j] in array[j]:
                        shuffle(required_elements)

            Board.set_column_in_array(array, required_elements, i)

        return row_7, row_8, row_9

    @staticmethod
    def pathways_with_columns(lis, ex_row_1, ex_row_2, ex_row_3):
        # We have to consider all 3 conditions (block, row and column) simultaneously
        block_11 = lis[0:3]
        block_12 = lis[3:6]
        block_13 = lis[6:9]
        block_21 = {}
        block_22 = {}
        block_23 = {}
        block_31 = {}
        block_32 = {}
        block_33 = {}

        row_2 = []
        row_3 = []

        for i in range(9):
            current_block = i//3+1
            col = Board.access_column([ex_row_1, ex_row_2, ex_row_3, lis], i)
            # Column condition
            required_elements = Board.get_sub_list([1,2,3,4,5,6,7,8,9], col)
            el = choice(required_elements)
            # Row condition
            while (el in block_21.keys() or el in block_22.keys() or el in block_23.keys()):
                el = choice(required_elements)
            # Block condition
            if current_block == 1:
                # For row 2 which is row 5 in rest of program
                while el in block_31.keys():
                    el = choice(required_elements)
                block_21[el] = i
                # For row 3 which is row 6 in rest of program
                if el in block_12 or el in block_32:
                    block_33[el] = 6   #* We will check about row 3 later on, so just add
                elif el in block_13 or el in block_33:
                    block_32[el] = 3
                else:
                    to_block = choice((2,3))
                    if to_block == 2:
                        block_32[el] = 3
                    else:
                        block_33[el] = 6
            elif current_block == 2:
                while el in block_32.keys():
                    el = choice(required_elements)
                block_22[el] = i
                if el in block_11 or el in block_31:
                    block_33[el] = 6
                elif el in block_13 or el in block_33:
                    block_31[el] = 0
                else:
                    to_block = choice((1,3))
                    if to_block == 1:
                        block_31[el] = 0
                    else:
                        block_33[el] = 6
            elif current_block == 3:
                while el in block_33.keys():
                    el = choice(required_elements)
                block_23[el] = i
                if el in block_12 or el in block_32:
                    block_31[el] = 0
                elif el in block_11 or el in block_31:
                    block_32[el] = 3
                else:
                    to_block = choice((1,2))
                    if to_block == 1:
                        block_31[el] = 0
                    else:
                        block_32[el] = 3

        for el, ind in block_21.items():
            row_2.insert(ind, el)
        for el, ind in block_22.items():
            row_2.insert(ind, el)
        for el, ind in block_23.items():
            row_2.insert(ind, el)

        # Now for row 3
        for el in block_31.keys():
            for i in range(3):
                col = Board.access_column([ex_row_1, ex_row_2, ex_row_3, lis, row_2], i)
                if el not in col:
                    block_31[el] = i # Update the index
        for el in block_32.keys():
            for i in range(3,6):
                col = Board.access_column([ex_row_1, ex_row_2, ex_row_3, lis, row_2], i)
                if el not in col:
                    block_32[el] = i # Update the index
        for el in block_33.keys():
            for i in range(6,9):
                col = Board.access_column([ex_row_1, ex_row_2, ex_row_3, lis, row_2], i)
                if el not in col:
                    block_33[el] = i # Update the index
        print(block_31)
        print(block_32)
        print(block_33)
        for el, ind in block_31.items():
            row_3.insert(ind, el)
        for el, ind in block_32.items():
            row_3.insert(ind, el)
        for el, ind in block_33.items():
            row_3.insert(ind, el)

        return row_2,row_3

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
    def remove_duplicates_from_dict(dic):
        new_dic = {}
        for key, val in dic.items():
            if val not in new_dic.values():
                new_dic[key] = val
        return new_dic

    # Final methods
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
        row_4 = STANDARD_LIST.copy()
        shuffle(row_4)
        # This process might be time consuming, so try an alternative if-possible
        valid = False
        while not valid:
            for i in range(9):
                column = Board.access_column([row_1, row_2, row_3], i)
                if row_4[i] in column:
                    shuffle(row_4)
                    break
            else:
                valid = True


        print("GOT ROW 4")
        # Using pathways with column condition for row 5 and row 6
        row_5, row_6 = Board.pathways_with_columns(row_4, row_1, row_2, row_3)

        print("GOT ROW 5 and 6")

        # Using method of remaining numbers to determine row 7,8 and 9
        row_7, row_8, row_9 = Board.get_final_three_blocks(
            row_1, row_2, row_3, row_4, row_5, row_6)

        print("GOT ROW 7,8,9")
        final = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]
        print(final)
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
