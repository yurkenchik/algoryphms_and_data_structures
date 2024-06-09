import unittest

from src.find_successor_in_order_traversal import find_successor, BinaryTree, find_bigger_successor

class TestInOrderTraversalNext(unittest.TestCase):

    def test_null(self):
        self.assertIsNone(find_successor(None))

    def test_next_in_order_with_right_child(self):
        root = BinaryTree(10)
        root.right = BinaryTree(20)
        next_node = find_bigger_successor(root)
        self.assertEqual(next_node, 20)

    def test_next_in_order_with_no_right_child(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.left.parent = root
        next_node = find_bigger_successor(root.left)
        self.assertEqual(next_node, 10)

    def test_next_in_order_with_parent(self):
        root = BinaryTree(10)
        left = BinaryTree(5)
        root.left = left
        left.parent = root
        next_node = find_bigger_successor(left)
        self.assertEqual(next_node, 10)

    def test_next_in_order_with_no_next_node(self):
        root = BinaryTree(10)
        next_node = find_bigger_successor(root)
        self.assertIsNone(next_node)

if __name__ == '__main__':
        unittest.main()