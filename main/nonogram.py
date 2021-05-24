import numpy as np


class Nonogram:

    # Initialise with grid array of a x a nonogram
    # additional list will be made for row and column for number clues
    def __init__(self, size):
        self._grid = np.zeros((size, size))
        self._column_clues = []
        self._row_clues = []

    @property
    def grid(self):
        return self._grid

    @property
    def column_clues(self):
        return self._column_clues

    @property
    def row_clues(self):
        return self._row_clues

    # input nonogram clues, with a space separating each number for each column/row
    def input_nonogram_numbers(self):
        # for the column clues
        i = 1
        while i <= len(self._grid):
            self.column_clues.append(input("Column " + str(i) + " clues are (separate by space): ").split())
            # convert to integers
            self.column_clues[i-1] = list(map(int, self.column_clues[i-1]))
            # check clue fits in the grid
            if sum(self.column_clues[i-1]) + len(self.column_clues[i-1]) - 1 > len(self._grid):
                print("Clue too large for nonogram, try again")
                self.column_clues.pop()
            else:
                i += 1
        # for the row clues
        i = 1
        while i <= len(self._grid):
            self.row_clues.append(input("Row " + str(i) + " clues are (separate by space): ").split())
            # convert to integers
            self.row_clues[i - 1] = list(map(int, self.row_clues[i - 1]))
            # check clue fits in the grid
            if sum(self.row_clues[i-1]) + len(self.row_clues[i-1]) - 1 > len(self._grid):
                print("Clue too large for nonogram, try again")
                self.row_clues.pop()
            else:
                i += 1

    # present nonogram grid with clues
    #def print_nonogram(self):

        #present_row_clues = np.array(self.row_clues)
        #print(present_row_clues)
