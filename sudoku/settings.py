import pickle


class Constants:

    try:
        with open("../data/user_settings.bin", 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        data = [0,0]    # By default

    # SCREEN PARAMETERS

    SCREEN_WIDTH = 625
    SCREEN_HEIGHT = 650
    SIDE_GAP = 12.5
    TOP_BOTTOM_GAP = 25

    # THEME

    THEME = ["LIGHT", "DARK"][data[0]]

    # DICT- {"THEME_NAME": [BG_COLOR, START_BOX_COLOR, UI_FONT_COLOR, SQUARES_COLOR, SQUARE_BORDER_COLOR,
    # SUDOKU_TEXT_COLOR_DEFAULT, SUDOKU_TEXT_COLOR_USER, TEMPLATE_COLOR, SELECTION_BOX_COLOR]}

    THEME_DICT = {"LIGHT":
                  [(255, 255, 255), (255, 255, 0), (255, 0, 0), (230, 230, 230), (150, 150, 150), (0, 0, 0), (100, 100, 100), (0, 0, 0),
                   (255, 165, 0)],
                  "DARK":
                  [(92, 64, 51), (178, 172, 136), (200, 200, 200), (200, 200, 200), (25, 25, 25), (100, 100, 100), (50, 50, 50),
                      (60, 60, 255), (255, 165, 0)]}

    # CELL PARAMETERS
    PADDING = 5

    # DIFFICULTY
    DIFFICULTY = ["EASY", "MEDIUM", "DIFFICULT"][data[1]]

    DIFFICULTY_DICT = {"EASY": 50, "MEDIUM": 40, "DIFFICULT": 30}
    d = {"SCREEN_WIDTH": SCREEN_WIDTH, "SCREEN_HEIGHT": SCREEN_HEIGHT, "THEME": THEME_DICT[THEME],
         "SIDE_GAP": SIDE_GAP, "TOP_BOTTOM_GAP": TOP_BOTTOM_GAP, "PADDING": PADDING,
         "DIFFICULTY": DIFFICULTY_DICT[DIFFICULTY]}

    # defaults is the list like:-
    # [<THEME_INDEX>, <DIFFICULTY_INDEX>]

    defaults = [0, 0]

    def __init__(self, make_defaults=False):
        # if make_defaults:
        # TODO: Should something be done?
        self.over_write_defaults(Constants.data[0], Constants.data[1])
        try:
            self.create_defaults()
        except FileExistsError:
            self.get_defaults()

    @staticmethod
    def create_defaults():
        with open("../data/user_settings.bin", 'xb') as file:
            pickle.dump(Constants.defaults, file)
        with open("../data/settings.bin", 'xb') as file:
            pickle.dump(Constants.d, file)

    @staticmethod
    def over_write_defaults(theme=0, difficulty=0):
        with open("../data/settings.bin", 'wb') as file:
            pickle.dump(Constants.d, file)

        with open("../data/user_settings.bin", 'wb') as file:
            pickle.dump([theme, difficulty], file)

    def get_defaults(self):
        with open("../data/settings.bin", 'rb') as file:
            data = pickle.load(file)
        self.d = data

    @classmethod
    def get_cell_side(cls):
        playable_side = cls.d["SCREEN_WIDTH"]-2*cls.d["SIDE_GAP"]
        cell_side = (playable_side - 8*cls.d["PADDING"])/9
        return cell_side


    @staticmethod
    def get_difficulty():
        with open("../data/user_settings.bin", 'rb') as file:
            data = pickle.load(file)
        return data[1]
