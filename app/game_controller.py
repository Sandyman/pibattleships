class GameController:
    def __init__(self, default_colour=(60, 80, 128)):
        self.__default_colour = default_colour

    def get(self, row, col):
        return self.__default_colour
