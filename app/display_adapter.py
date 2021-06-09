from collections import defaultdict


class DisplayAdapter:
    """
    This class is an adapter between the data model and the
    SenseHat display. It retrieves the pixels from the model
    and builds a pixel image that can be presented to the
    SenseHat display in one go using the {set_pixels} API
    call.
    """
    def __init__(self, sensehat, model, colour_map=None, rows=8, columns=8):
        self.__sensehat = sensehat
        self.__model = model

        if colour_map is None:
            colour_map = defaultdict(lambda: (0, 0, 0))

        self.__colour_map = colour_map

        self.__rows = rows
        self.__columns = columns

    def update(self):
        """
        Update the display. This will get all the pixels from
        the model row-by-row. The model must support a method
        {get} which must accepts as arguments (row, col).
        """
        model = self.__model
        cols = self.__columns
        rows = self.__rows
        colmap = self.__colour_map
        pixels = [colmap[model.get(row, col)]
                  for row in range(rows)
                  for col in range(cols)]
        self.__sensehat.set_pixels(pixels)
