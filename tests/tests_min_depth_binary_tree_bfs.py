import unittest
from src.min_depth_binary_tree_bfs import min_depth_binary_tree_bfs, read_binary_tree_input


class TestBinaryTreeDepth(unittest.TestCase):
    def test_depth(self):
        with open("../src/resources/input.txt", "r") as f:
            root_id = int(f.readline())
            edges = [tuple(map(int, line.strip().split(","))) for line in f]

        adjacency_list = {}
        for u, v in edges:
            if u in adjacency_list:
                adjacency_list[u].append(v)
            else:
                adjacency_list[u] = [v]

        expected_depth = 3
        actual_depth = min_depth_binary_tree_bfs(root_id, adjacency_list)
        self.assertEqual(expected_depth, actual_depth)

    def test_empty_tree(self):
        expected_depth = 0
        root_id = None
        actual_depth = min_depth_binary_tree_bfs(root_id, {})
        self.assertEqual(expected_depth, actual_depth)

