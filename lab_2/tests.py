import unittest
from lab2_lev3_var1 import find_max_number_of_hamsters


class TestMaxNumberOfHamstersFunction(unittest.TestCase):

    def test_case_1(self):

        S = 7
        C = 3
        hamsters_test_array = [[1, 2], [2, 2], [3, 1]]

        self.assertEqual(find_max_number_of_hamsters(S, C, hamsters_test_array), 2)

    def test_case_2(self):

        S = 19
        C = 4
        hamsters_test_array = [[5, 0], [2, 2], [1, 4], [5, 1]]

        self.assertEqual(find_max_number_of_hamsters(S, C, hamsters_test_array), 3)

    def test_case_3(self):

        S = 2
        C = 2
        hamsters_test_array = [[1, 50000], [1, 60000]]

        self.assertEqual(find_max_number_of_hamsters(S, C, hamsters_test_array), 1)

if __name__ == "__main__":
    unittest.main()