import unittest

from ..src.zigzag_traversal import arr_zigzag_traversed

class Lab1Test(unittest.TestCase):
    def test_arr_zigzag_5x5(self):

        test_array = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        test_rows_length = 5
        test_columns_length = 5
        needed_result = [25, 24, 20, 15, 19, 23, 22, 18, 14, 10, 5, 9, 13, 17, 21, 16, 12, 8, 4, 3, 7, 11, 6, 2, 1]
        self.assertEqual(arr_zigzag_traversed(test_array, test_rows_length, test_columns_length), needed_result, "error!")

    def test_arr_zigzag_2x4(self):
        test_array = [[1, 2, 3, 4],
                      [5, 6, 7, 8]]

        test_rows_length = 2
        test_columns_length = 4

        needed_result = [8, 7, 4, 3, 6, 5, 2, 1]
        self.assertEqual(arr_zigzag_traversed(test_array, test_rows_length, test_columns_length), needed_result, "error!")

    def test_arr_zigzag_1x6(self):
        test_array = [[1, 2, 3, 4, 5, 6]]

        test_rows_length = 1
        test_columns_length = 6

        needed_result = [6, 5, 4, 3, 2, 1]
        self.assertEqual(arr_zigzag_traversed(test_array, test_rows_length, test_columns_length), needed_result, "error!")

    def test_arr_zigzag_1x1(self):
        test_array = [[1]]

        test_rows_length = 1
        test_columns_length = 1

        needed_result = [1]
        self.assertEqual(arr_zigzag_traversed(test_array, test_rows_length, test_columns_length), needed_result,
                         "error!")

    def test_arr_zigzag_empty(self):
        test_array = []

        test_rows_length = 0
        test_columns_length = 0

        needed_result = []
        self.assertEqual(arr_zigzag_traversed(test_array, test_rows_length, test_columns_length), needed_result,
                         "error!")

if __name__ == "__main__":
    unittest.main()