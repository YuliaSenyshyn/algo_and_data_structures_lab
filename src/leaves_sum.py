class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def leavesSum(root):
    def helper(node, is_left_child):
        if not node:
            return 0
        if not node.left and not node.right and is_left_child:
            return node.value
        return helper(node.left, True) + helper(node.right, False)

    return helper(root, False)