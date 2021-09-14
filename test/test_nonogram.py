from main.nonogram import Nonogram
import numpy as np
from unittest.mock import patch


class TestNonogram:

    def test_nonogram_creates_correct_matrix_size_and_value(self):
        smile = Nonogram(3)
        # assert size is correct
        assert np.size(smile.grid) == 3 * 3
        # assert that the matrix only contains capital o's as strings)
        assert np.all((smile.grid == 'O')) == True

    @patch('builtins.input', side_effect=["1 1", "2", "0", "2", "1", "1"])
    def test_input_clues_work_correctly(self, mock):
        smile = Nonogram(3)
        smile.input_nonogram_numbers()
        assert smile.column_clues == [[1, 1], [2], [0]]
        assert smile.row_clues == [[2], [1], [1]]

    @patch('builtins.input', side_effect=["1 1", "2", "0", "2", "1", "1"])
    def test_large_single_clue(self, mock):
        smile = Nonogram(3)
        smile.input_nonogram_numbers()
        smile.solve_large_single_clue()
        assert smile.grid[1][1] == "*"
        assert smile.grid[0][1] == "*"

    @patch('builtins.input', side_effect=["1", "6", "5 1", "1 1 1", "4 1 1 1", "1 1 1 1 1", "1 1 1 1 1", "1 1 1 3",
                                          "1 1 1 1 1", "1 1 1 1 1", "4 1 1 1", "1 1 1", "5 1", "6", "1", "7", "1 1",
                                          "1 1", "11", "1 1", "1 1", "1 1", "13", "1 1", "1 1", "1 1", "1 1", "15", "1",
                                          "7"])
    def test_large_single_clue_2(self, mock):
        smile = Nonogram(15)
        smile.input_nonogram_numbers()
        smile.solve_large_single_clue()
        print(smile.grid)
        answer = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', '*', '*', '*', '*', '*', '*', '*', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]
        print(np.all((smile.grid == answer)))
        assert np.all((smile.grid == answer)) == True


