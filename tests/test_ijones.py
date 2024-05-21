import unittest
from src.indiana_jones_rectangular_treasure import indiana_jones_traversal, read_input_matrix, read_output


class TestIndianaJonesTraversal(unittest.TestCase):
    def test_indiana_jones_traversal(self):
        # Read input matrix and expected output from files
        row_size, col_size, sneaky_way = read_input_matrix("../src/sources/i_jones1.in")

        # Call the function with the provided data
        result = indiana_jones_traversal(sneaky_way, rows=row_size, cols=col_size)

        # Check if the result matches the expected output
        self.assertEqual(result, 32)

    def test_indiana_jones_traversal2(self):
        # Read input matrix and expected output from files
        row_size, col_size, sneaky_way = read_input_matrix("../src/sources/i_jones2.in")

        # Call the function with the provided data
        result = indiana_jones_traversal(sneaky_way, rows=row_size, cols=col_size)

        # Check if the result matches the expected output
        self.assertEqual(result, 64)

    def test_indiana_jones_traversal3(self):
        # Read input matrix and expected output from files
        row_size, col_size, sneaky_way = read_input_matrix("../src/sources/i_jones3.in")

        # Call the function with the provided data
        result = indiana_jones_traversal(sneaky_way, rows=row_size, cols=col_size)

        # Check if the result matches the expected output
        self.assertEqual(result, 3352)


if __name__ == '__main__':
    unittest.main()