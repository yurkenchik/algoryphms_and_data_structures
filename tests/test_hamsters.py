import unittest

from src.hasmters_lab import max_number_of_hamsters

class TestMaxNumberOfHamstersFunction(unittest.TestCase):

    def test_case_1(self):

        S = 7
        C = 3
        hamsters_test_array = [[1, 2], [2, 2], [3, 1]]

        self.assertEqual(max_number_of_hamsters(S, C, hamsters_test_array), 2)

    def test_case_2(self):

        S = 19
        C = 4
        hamsters_test_array = [[5, 0], [2, 2], [1, 4], [5, 1]]

        self.assertEqual(max_number_of_hamsters(S, C, hamsters_test_array), 3)

    def test_case_3(self):

        S = 2
        C = 2
        hamsters_test_array = [[1, 50000], [1, 60000]]

        self.assertEqual(max_number_of_hamsters(S, C, hamsters_test_array), 1)

    def test_case_4(self):

        S = 1000
        C = 9
        hamsters_test_array = [[10000, 1],
                      [1000, 1],
                      [3000, 1],
                      [500, 1],
                      [300, 1],
                      [700, 1],
                      [600, 1],
                      [400, 2],
                      [50, 80]]

        self.assertEqual(max_number_of_hamsters(S, C, hamsters_test_array), 3)

if __name__ == "__main__":
    unittest.main()