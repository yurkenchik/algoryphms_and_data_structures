import unittest

from algoryphms_and_data_structures.src.game_server_latency import best_server_place, parse_data_from_file

class Test(unittest.TestCase):

    def test_game_server1(self):
        adjacency_list, client_nodes = parse_data_from_file("sources/game_server_inputs/game_server1.in")
        res = best_server_place(adjacency_list, client_nodes)
        self.assertEqual((100, 4), res)

    def test_game_server2(self):
        adjacency_list, client_nodes = parse_data_from_file("sources/game_server_inputs/game_server2.in")
        res = best_server_place(adjacency_list, client_nodes)
        self.assertEqual((10, 5), res)

    def test_game_server3(self):
        adjacency_list, client_nodes = parse_data_from_file("sources/game_server_inputs/game_server3.in")
        res = best_server_place(adjacency_list, client_nodes)
        self.assertEqual((1000000000, 2), res)