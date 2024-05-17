import unittest

from src.avl_priority_queue import AvlTree, AvlTreeNode

class TestAvlTreeMethods(unittest.TestCase):

    def setUp(self):
        self.tree = AvlTree()

    def test_insertion_and_in_order_traversal(self):
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 1, 2)
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 2, 2)
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 3, 2)
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 4, 1)
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 5, 3)
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 6, 2)

        expected_result = [4, 1, 2, 3, 6, 5]
        self.assertEqual(self.tree.in_order_traversal(self.tree.root), expected_result)

    def test_deletion_and_in_order_traversal(self):
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 1, 1)
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 2, 2)
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 3, 2)
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 4, 1)
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 5, 3)
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 6, 2)

        self.tree.root = self.tree.deletion_by_priority(self.tree.root, 3)
        self.tree.root = self.tree.deletion_by_priority(self.tree.root, 2)

        expected_result = [1, 4, 3, 6]
        self.assertEqual(self.tree.in_order_traversal(self.tree.root), expected_result)

    def test_height_difference_calculation(self):
        node = AvlTreeNode(1, 1)
        node.left = AvlTreeNode(2, 2)
        node.right = AvlTreeNode(3, 2)

        height_difference = self.tree.height_difference_between_left_and_right_subtrees(node)
        self.assertEqual(height_difference, 0)

    def test_deletion_of_not_existing_node(self):
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 3, 1)
        self.tree.root = self.tree.insertion_by_priority(self.tree.root, 2, 2)

        self.tree.root = self.tree.deletion_by_priority(self.tree.root, 4)
        expected_result = [3, 2]

        self.assertEqual(self.tree.in_order_traversal(self.tree.root), expected_result)

if __name__ == '__main__':
    unittest.main()
