class DataModel:
    def __init__(self, rows=8, columns=8):
        self.__rows = 8
        self.__columns = 8

        self.__data = [list([None] * rows)] * columns

    def put(self, row, column, item):
        """
        Put {item} at location ({row}, {column}).
        :param row: Row of location for {item}
        :param column: Column of location for {item}
        :param item: Item to place at position
        """
        self.__data[row][column] = item

    def get(self, row, column):
        """
        Get item at location (row, column).
        :param row: Row of cell to retrieve
        :param column: Column of cell to retrieve
        :return: Contents of cell

        """
        return self.__data[row][column]
