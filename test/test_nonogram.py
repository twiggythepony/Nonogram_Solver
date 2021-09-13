from main.nonogram import Nonogram
import numpy as np


class TestNonogram:

    def test_nonogram_creates_correct_matrix_size_and_value(self):
        smile = Nonogram(3)
        print(smile.grid)
        #assert size is correct
        assert np.size(smile.grid) == 3 * 3
        # assert that the matrix only contains capital o's as strings)
        assert np.all((smile.grid == 'O')) == True

    def test_input_clues_work_correctly(self):
        smile = Nonogram(3)
        smile.input_nonogram_numbers()
        # print(smile.column_clues)
        # print(smile.row_clues)

        # assert survivor.name == "Judy"
