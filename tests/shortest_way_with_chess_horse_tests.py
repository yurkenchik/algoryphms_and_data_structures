import unittest

from algo_and_data_structures_course.src.shortest_way_with_chess_horse import minimal_number_of_moves

class TestMinimalNumberOfMoves(unittest.TestCase):
    def test_minimal_number_of_moves_case_1(self):
        with open("sources/input.txt", "w") as file:
            file.write("12\n")
            file.write("11, 0\n")
            file.write("0, 11\n")

        start_position = (11, 0)
        end_position = (0, 11)
        expected_result = 8

        result = minimal_number_of_moves(start_position, end_position)

        self.assertEqual(result, expected_result)

    def test_minimal_number_of_moves_case_2(self):
        with open("sources/input.txt", "w") as file:
            file.write("16\n")
            file.write("0, 0\n")
            file.write("0, 15\n")

        start_position = (0, 0)
        end_position = (0, 15)
        expected_result = 6

        result = minimal_number_of_moves(start_position, end_position)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
