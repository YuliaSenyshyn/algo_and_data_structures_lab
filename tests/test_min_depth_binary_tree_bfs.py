import unittest
from src.min_depth_binary_tree_bfs import BinaryTree


class TestBinaryTree(unittest.TestCase):
    def test_add_and_remove_max_priority(self):
        binary_tree = BinaryTree()
        binary_tree.add(5, 3)
        binary_tree.add(3, 2)
        binary_tree.add(8, 4)
        binary_tree.add(7, 1)

        self.assertEqual(binary_tree.remove_max_priority(), 8)
        self.assertEqual(binary_tree.remove_max_priority(), 5)
        self.assertEqual(binary_tree.remove_max_priority(), 3)
        self.assertEqual(binary_tree.remove_max_priority(), 7)
        self.assertIsNone(binary_tree.remove_max_priority())  # Ensure None is returned when tree is empty

    def test_inorder_tree(self):
        binary_tree = BinaryTree()
        binary_tree.add(5, 3)
        binary_tree.add(3, 2)
        binary_tree.add(8, 4)
        binary_tree.add(7, 1)

        expected_order = [4, 3, 2, 1]
        observed_order = []

        def inorder_traverse(node):
            if node is None:
                return
            inorder_traverse(node.right)
            observed_order.append(node.priority)
            inorder_traverse(node.left)

        inorder_traverse(binary_tree.root)
        self.assertEqual(observed_order, expected_order)

if __name__ == '__main__':
    unittest.main()