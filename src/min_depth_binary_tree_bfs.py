class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value, priority):
        if not self.root:
            self.root = Node(value, priority)
        else:
            self._add_recursive(self.root, value, priority)

    def _add_recursive(self, node, value, priority):
        if priority <= node.priority:
            if node.left is None:
                node.left = Node(value, priority)
            else:
                self._add_recursive(node.left, value, priority)
        else:
            if node.right is None:
                node.right = Node(value, priority)
            else:
                self._add_recursive(node.right, value, priority)

    def remove_max_priority(self):
        if self.root is None:
            return None

        max_node, parent = self._find_max_node_and_parent(self.root, None)
        if parent is None:
            self.root = max_node.left
        else:
            parent.right = max_node.left
        return max_node.value

    def _find_max_node_and_parent(self, node, parent):
        if node.right is None:
            return node, parent
        return self._find_max_node_and_parent(node.right, node)


    def inorder_tree(self, node):
        if node is None:
            return

        self.inorder_tree(node.right)
        print(node.priority)
        self.inorder_tree(node.left)