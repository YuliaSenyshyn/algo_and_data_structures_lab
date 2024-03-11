import unittest
from src.leaves_sum import leavesSum, BinaryTree

class TestLeavesSum(unittest.TestCase):
    def test_leaves_sum(self):
        root = BinaryTree(4)
        root.left = BinaryTree(10)
        root.right = BinaryTree(21)
        root.right.left = BinaryTree(16)
        root.right.right = BinaryTree(8)

        self.assertEqual(leavesSum(root), 26)

        self.assertEqual(leavesSum(None), 0)

if __name__ == '__main__':
    unittest.main()