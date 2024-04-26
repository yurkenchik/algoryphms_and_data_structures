
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_successor(node: BinaryTree) -> BinaryTree:

    if node is None:
        return None

    if node.right:
        node = node.right
        while node.left is not None:
            node = node.left
        return node

    while node.parent and node.parent.right == node:
        node = node.parent

    return node.parent

def find_bigger_successor(node: BinaryTree) -> BinaryTree:
    next_node = find_successor(node)
    if not next_node:
        return None
    while next_node and next_node.value <= node.value:
        next_node = find_successor(next_node)
    return next_node.value
