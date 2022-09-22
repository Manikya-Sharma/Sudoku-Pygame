import pickle


class Constants:
    SCREEN_WIDTH =650
    SCREEN_HEIGHT = 650

    d = {"SCREEN_WIDTH":SCREEN_WIDTH, "SCREEN_HEIGHT":SCREEN_HEIGHT}

    def __init__(self, make_defaults = False):
        if make_defaults:
            self.over_write_defaults()
        try:
            self.create_defaults()
        except FileExistsError:
            self.get_defaults()

    def create_defaults(self):
        with open("./data/settings.bin", 'xb') as file:
            pickle.dump(Constants.d, file)

    def over_write_defaults(self):
        with open("./data/settings.bin", 'wb') as file:
            pickle.dump(Constants.d, file)

    def get_defaults(self):
        with open("./data/settings.bin",'rb') as file:
            data = pickle.load(file)
        self.d = data
