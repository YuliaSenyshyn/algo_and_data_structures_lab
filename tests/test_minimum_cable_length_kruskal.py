import unittest
from src.minimum_cable_length_kruskal import kruskals_algo, read_graph_from_csv


class TestKruskalsAlgo(unittest.TestCase):
    def test_kruskals_algo(self):
        graph = [
            [0, 10, 5, 15, 20],
            [10, 0, 7, 12, 18],
            [5, 7, 0, 8, 13],
            [15, 12, 8, 0, 11],
            [20, 18, 13, 11, 0]
        ]
        min_weight, _ = kruskals_algo(graph)
        self.assertEqual(min_weight, 31)


class TestMinimumCableLength(unittest.TestCase):
    def test_minimum_cable_length(self):
        graph = read_graph_from_csv('src/resources/island.csv')
        min_weight, _ = kruskals_algo(graph)

        with open('src/resources/output.island', 'r') as file:
            expected_result = int(file.read().strip())

        self.assertEqual(min_weight, expected_result)


class TestFileNotEmpty(unittest.TestCase):
    def test_file_not_empty(self):
        graph = read_graph_from_csv('src/resources/island.csv')
        self.assertTrue(graph, "The file 'island.csv' is empty")


if __name__ == '__main__':
    unittest.main()
