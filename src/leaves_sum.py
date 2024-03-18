class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def leavesSum(root):
    def helper(node, is_right_child):
        if not node:
            return 0
        if not node.left and not node.right and is_right_child:
            return node.value
        return helper(node.left, False) + helper(node.right, True)

    return helper(root, True)

