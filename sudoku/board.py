import pygame
from random import shuffle, choice
from cell import Cell
from loading_screen import Loading
from settings import Constants


class Board:
    """
    *    METHOD OF PATHWAYS
        To get 3 blocks satisfying the block, row and column condition
        only two possible pathways are possible for an element
        (ignoring internal arrangements)

    *     1.                    2.

    *     [•]   []   []         [•]   []   []

    *     []   [•]   []         []   []   [•]

    *     []   []   [•]         []   [•]   []
    """

    # Initialization Functions
    @staticmethod
    def get_final_three_blocks(ex_row_1, ex_row_2, ex_row_3, ex_row_4, ex_row_5, ex_row_6):
        keep_trying = True
        while keep_trying:
            row_7 = []
            row_8 = []
            row_9 = []
            array = [row_7, row_8, row_9]
            for i in range(9):   # The columns
                existing_in_column = Board.access_column(
                    [ex_row_1, ex_row_2, ex_row_3, ex_row_4, ex_row_5, ex_row_6], i)

                available_elements = Board.get_sub_list(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9], existing_in_column)
                valid = False
                count = 0
                while not valid:
                    shuffle(available_elements)
                    for j in range(3):
                        if available_elements[j] in array[j]:
                            valid = False
                            count += 1
                            break
                    else:
                        valid = True
                        Board.set_column_in_array(array, available_elements, i)
                    # Too many iterations, maybe wrong choices were made initially
                    if count >= 1000:
                        # print("Thats enough!")
                        # Could have used better approach by thinking several cases
                        # but as permutations are comparatively less, so its fine
                        keep_trying = True
                        break_for = True
                        break
                    else:
                        break_for = False
                else:
                    keep_trying = False
                if break_for:
                    break
        return row_7, row_8, row_9

    @staticmethod
    def pathways_with_columns(lis, ex_row_1, ex_row_2, ex_row_3):
        # We have to consider all 3 conditions (block, row and column) simultaneously
        valid_blocks = False
        while not valid_blocks:
            existing = {1: lis[0:3], 2: lis[3:6], 3: lis[6:9]}
            next_ones = {1: [], 2: [], 3: []}
            next_to_next_ones = {1: [], 2: [], 3: []}

            row_5 = []
            row_6 = []

            for existing_block, elements_list in existing.items():
                for element in elements_list:
                    # If in block 1
                    if existing_block == 1:
                        next_block = choice((2, 3))
                        if next_block == 2:
                            count_invalid_places = 0
                            for i in range(3, 6):
                                col = Board.access_column(
                                    [ex_row_1, ex_row_2, ex_row_3], i)
                                if element in col:
                                    count_invalid_places += 1
                            if (count_invalid_places >= 3 or
                                len(next_ones[2]) >= 3 or
                                    len(next_to_next_ones[3]) >= 3):    # Nowhere possible
                                next_ones[3].append(element)
                                next_to_next_ones[2].append(element)
                                continue
                            else:
                                next_ones[2].append(element)
                                next_to_next_ones[3].append(element)
                                continue
                        if next_block == 3:
                            count_invalid_places = 0
                            for i in range(6, 9):
                                col = Board.access_column(
                                    [ex_row_1, ex_row_2, ex_row_3], i)
                                if element in col:
                                    count_invalid_places += 1
                            if (count_invalid_places >= 3 or
                                len(next_ones[3]) >= 3 or
                                    len(next_to_next_ones[2]) >= 3):    # Nowhere possible
                                next_ones[2].append(element)
                                next_to_next_ones[3].append(element)
                                continue
                            else:
                                next_ones[3].append(element)
                                next_to_next_ones[2].append(element)
                                continue
                    # If in block 2
                    if existing_block == 2:
                        next_block = choice((1, 3))
                        if next_block == 1:
                            count_invalid_places = 0
                            for i in range(0, 3):
                                col = Board.access_column(
                                    [ex_row_1, ex_row_2, ex_row_3], i)
                                if element in col:
                                    count_invalid_places += 1
                            if (count_invalid_places >= 3 or
                                len(next_ones[1]) >= 3 or
                                    len(next_to_next_ones[3]) >= 3):    # Nowhere possible
                                next_ones[3].append(element)
                                next_to_next_ones[1].append(element)
                                continue
                            else:
                                next_ones[1].append(element)
                                next_to_next_ones[3].append(element)
                                continue
                        if next_block == 3:
                            count_invalid_places = 0
                            for i in range(6, 9):
                                col = Board.access_column(
                                    [ex_row_1, ex_row_2, ex_row_3], i)
                                if element in col:
                                    count_invalid_places += 1
                            if (count_invalid_places >= 3 or
                                len(next_ones[3]) >= 3 or
                                    len(next_to_next_ones[1]) >= 3):    # Nowhere possible
                                next_ones[1].append(element)
                                next_to_next_ones[3].append(element)
                                continue
                            else:
                                next_ones[3].append(element)
                                next_to_next_ones[1].append(element)
                                continue
                    # If in block 3
                    if existing_block == 3:
                        next_block = choice((1, 2))
                        if next_block == 1:
                            count_invalid_places = 0
                            for i in range(0, 3):
                                col = Board.access_column(
                                    [ex_row_1, ex_row_2, ex_row_3], i)
                                if element in col:
                                    count_invalid_places += 1
                            if (count_invalid_places >= 3 or
                                len(next_ones[1]) >= 3 or
                                    len(next_to_next_ones[2]) >= 3):    # Nowhere possible
                                next_ones[2].append(element)
                                next_to_next_ones[1].append(element)
                                continue
                            else:
                                next_ones[1].append(element)
                                next_to_next_ones[2].append(element)
                                continue
                        if next_block == 2:
                            count_invalid_places = 0
                            for i in range(3, 6):
                                col = Board.access_column(
                                    [ex_row_1, ex_row_2, ex_row_3], i)
                                if element in col:
                                    count_invalid_places += 1
                            if (count_invalid_places >= 3 or
                                len(next_ones[2]) >= 3 or
                                    len(next_to_next_ones[1]) >= 3):    # Nowhere possible
                                next_ones[1].append(element)
                                next_to_next_ones[2].append(element)
                                continue
                            else:
                                next_ones[2].append(element)
                                next_to_next_ones[1].append(element)
                                continue

            # Now we need to only shuffle the blocks ensuring column condition

            # Row 5
            for j in range(3):   # A block
                valid = False
                count = 0
                while not valid:
                    shuffle(next_ones[j+1])
                    for i in range(3):   # Each element of block
                        if (next_ones[j+1][i] in
                                Board.access_column([ex_row_1, ex_row_2, ex_row_3], (j)*3+i)):
                            valid = False
                            count += 1
                            break
                    else:
                        valid = True
                    if count >= 1000:  # Maybe some wring choices initially
                        break_for = True
                        break
                    else:
                        break_for = False
                if break_for:
                    valid_blocks = False
                    break_complete = True
                    break
                # Out of loop must be valid
                else:
                    break_complete = False
                    row_5.extend(next_ones[j+1])
            if break_complete:
                break

            # Row 6
            for j in range(3):   # A block
                valid = False
                count = 0
                while not valid:
                    shuffle(next_to_next_ones[j+1])
                    for i in range(3):   # Each element of block
                        if (next_to_next_ones[j+1][i] in
                                Board.access_column([ex_row_1, ex_row_2, ex_row_3], (j)*3+i)):
                            valid = False
                            count += 1
                            break
                    else:
                        valid = True
                    if count >= 1000:
                        break_for = True
                        break
                    else:
                        break_for = False
                if break_for:
                    valid_blocks = False
                    break_complete = True
                    break
                # Out of loop must be valid
                else:
                    break_complete = False
                    row_6.extend(next_to_next_ones[j+1])
            if break_complete:
                break
            else:
                valid_blocks = True   # Finally, must be correct
        return row_5, row_6

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

    # Final methods
    @staticmethod
    def get_sudoku_array(screen):
        load = Loading(screen, 5)
        load.draw_and_update()
        STANDARD_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        valid_columns = False
        while not valid_columns:
            # Get first row
            row_1 = STANDARD_LIST.copy()
            shuffle(row_1)

            load.set_zero()
            load.increment_loading()
            load.draw_and_update()

            # Get the 3 blocks through pathways
            row_2, row_3 = Board.pathways(row_1)

            load.increment_loading()
            load.draw_and_update()

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

            load.increment_loading()
            load.draw_and_update()

            # Using pathways with column condition for row 5 and row 6
            row_5, row_6 = Board.pathways_with_columns(
                row_4, row_1, row_2, row_3)

            load.increment_loading()
            load.draw_and_update()

            # Now check that no two columns are same
            # (Because in such case, last 3 rows cant be filled)
            for i in range(9):
                column_1 = Board.access_column(
                    [row_1, row_2, row_3, row_4, row_5, row_6], i)
                for j in range(9):
                    if i == j:
                        continue
                    column_2 = Board.access_column(
                        [row_1, row_2, row_3, row_4, row_5, row_6], j)
                    # All same
                    if Board.get_num_common_elements(column_1, column_2) >= 6:
                        valid_columns = False
                        break_for = True
                        break
                    else:
                        break_for = False
                if break_for:
                    break
            else:
                valid_columns = True

        # Using method of remaining numbers to determine row 7,8 and 9
        row_7, row_8, row_9 = Board.get_final_three_blocks(
            row_1, row_2, row_3, row_4, row_5, row_6)

        load.increment_loading()
        load.draw_and_update()

        final = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]
        return final

    @staticmethod
    def initialize_cells(screen):
        # Number of defaults
        c = Constants()
        num_given = c.d["DIFFICULTY"]
        num_done = 0

        final = Board.get_sudoku_array(screen)
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

    # Functions which work throughout
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
            row.insert(column, elements_list[i])
            i += 1

    @staticmethod
    def remove_duplicates_from_dict(dic):
        new_dic = {}
        for key, val in dic.items():
            if val not in new_dic.values():
                new_dic[key] = val
        return new_dic
