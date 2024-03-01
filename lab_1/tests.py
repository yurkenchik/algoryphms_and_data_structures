import unittest
from algo_and_data_structures_course.lab_1.lab1_lev3_var1 import arr_zigzag_traverse

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
        needed_result = [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 21, 17, 13,
                         9, 5, 10, 14, 18, 22, 23, 19, 15, 20, 24, 25]
        self.assertEqual(arr_zigzag_traverse(test_array, test_rows_length, test_columns_length), needed_result, "error!")

    def test_arr_zigzag_2x4(self):
        test_array = [[1, 2, 3, 4],
                      [5, 6, 7, 8]]

        test_rows_length = 2
        test_columns_length = 4

        needed_result = [1, 2, 5, 6, 3, 4, 7, 8]
        self.assertEqual(arr_zigzag_traverse(test_array, test_rows_length, test_columns_length), needed_result, "error!")

    def test_arr_zigzag_1x6(self):
        test_array = [[1, 2, 3, 4, 5, 6]]

        test_rows_length = 1
        test_columns_length = 6

        needed_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(arr_zigzag_traverse(test_array, test_rows_length, test_columns_length), needed_result, "error!")

    def test_arr_zigzag_1x1(self):
        test_array = [[1]]

        test_rows_length = 1
        test_columns_length = 1

        needed_result = [[1]]
        self.assertEqual(arr_zigzag_traverse(test_array, test_rows_length, test_columns_length), needed_result,
                         "error!")

if __name__ == "__main__":
    unittest.main()