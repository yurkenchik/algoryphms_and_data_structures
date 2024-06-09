import unittest

from src.islands import minimal_length_of_cables_counter, read_graph_from_csv

class TestMinimalLengthOfCablesCounter(unittest.TestCase):
    def test_minimal_length_of_cables_counter(self):
        # Read graph data from CSV file
        vertices, graph = read_graph_from_csv('../src/sources/islands_input.csv')

        # Calculate minimal length of cables and minimal spanning tree
        min_length, minimal_spanning_tree = minimal_length_of_cables_counter(vertices, graph)

        # Expected minimal length of cables and minimal spanning tree
        expected_min_length = 11
        expected_minimal_spanning_tree = [
            [0, 2, 1],
            [0, 1, 2],
            [0, 3, 8]
        ]

        # Assert the results
        self.assertEqual(min_length, expected_min_length)
        self.assertEqual(minimal_spanning_tree, expected_minimal_spanning_tree)

    def test_minimal_length_of_cables_counter2(self):
        # Read graph data from CSV file
        vertices, graph = read_graph_from_csv('../src/sources/islands/islands_input2.csv')

        # Calculate minimal length of cables and minimal spanning tree
        min_length, minimal_spanning_tree = minimal_length_of_cables_counter(vertices, graph)

        # Expected minimal length of cables and minimal spanning tree
        expected_min_length = 19
        expected_minimal_spanning_tree = [
            [2, 3, 4],
            [0, 3, 5],
            [0, 1, 10]
        ]

        # Assert the results
        self.assertEqual(min_length, expected_min_length)
        self.assertEqual(minimal_spanning_tree, expected_minimal_spanning_tree)

    def test_minimal_length_of_cables_counter3(self):
        # Read graph data from CSV file
        vertices, graph = read_graph_from_csv('../src/sources/islands/islands_input3.csv')

        # Calculate minimal length of cables and minimal spanning tree
        min_length, minimal_spanning_tree = minimal_length_of_cables_counter(vertices, graph)

        # Expected minimal length of cables and minimal spanning tree
        expected_min_length = 9
        expected_minimal_spanning_tree = [
            [0, 1, 4],
            [0, 3, 5],
        ]

        # Assert the results
        self.assertEqual(min_length, expected_min_length)
        self.assertEqual(minimal_spanning_tree, expected_minimal_spanning_tree)


if __name__ == '__main__':
    unittest.main()