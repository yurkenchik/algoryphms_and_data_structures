
class AvlTreeNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

class AvlTree:
    def __init__(self):
        self.root = None

    def height_determiner(self, node):
        if not node:
            return 0

        return node.height

    def insertion_by_priority(self, node, node_to_insert, priority):

        if node is None:
            return AvlTreeNode(node_to_insert, priority)

        elif priority < node.priority:
            node.left = self.insertion_by_priority(node.left, node_to_insert, priority)
        else:
            node.right = self.insertion_by_priority(node.right, node_to_insert, priority)

        node.height = 1 + max(self.height_determiner(node.left), self.height_determiner(node.right))
        height_difference = self.height_difference_between_left_and_right_subtrees(node)

        if height_difference > 1 and node_to_insert < node.left.value:
            return self.right_rotate(node)

        if height_difference < -1 and node_to_insert > node.right.value:
            return self.left_rotate(node)

        if height_difference > 1 and node_to_insert > node.left.value:
            node.left = self.left_rotate(node.right)
            return self.right_rotate(node)

        if height_difference < -1 and node_to_insert < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def node_with_minimal_value(self, node):
        current_node = node

        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def deletion_by_priority(self, node, priority):
        if node is None:
            return node

        if priority < node.priority:
            node.left = self.deletion_by_priority(node.left, priority)
        elif priority > node.priority:
            node.right = self.deletion_by_priority(node.right, priority)
        else:
            if node.left is None:
                node_to_swap = node.right
                node = None
                return node_to_swap
            elif node.right is None:
                node_to_swap = node.left
                node = None
                return node_to_swap

            node_to_swap = self.node_with_minimal_value(node.right)
            node.value = node_to_swap.value
            node.priority = node_to_swap.priority
            node.right = self.deletion_by_priority(node.right, node_to_swap.priority)

        if node is None:
            return node

        node.height = 1 + max(self.height_determiner(node.left), self.height_determiner(node.right))
        height_difference = self.height_difference_between_left_and_right_subtrees(node)

        if height_difference > 1 and self.height_determiner(node.left.left) >= self.height_determiner(node.left.right):
            return self.right_rotate(node)

        if height_difference < -1 and self.height_determiner(node.right.right) >= self.height_determiner(node.right.left):
            return self.left_rotate(node)

        if height_difference > 1 and self.height_determiner(node.left.right) > self.height_determiner(node.left.left):
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if height_difference < -1 and self.height_determiner(node.right.left) > self.height_determiner(
                node.right.right):
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def right_rotate(self, parent_node):
        left_child = parent_node.left
        link_to_y = left_child.right
        left_child.right = parent_node
        parent_node.left = link_to_y

        parent_node.height = 1 + max(self.height_determiner(parent_node.left), self.height_determiner(parent_node.right))
        left_child.height = 1 + max(self.height_determiner(left_child.left), self.height_determiner(left_child.right))

        return left_child

    def left_rotate(self, parent_node):
        left_child = parent_node.right
        link_to_y = left_child.left
        left_child.left = parent_node
        parent_node.right = link_to_y

        parent_node.height = 1 + max(self.height_determiner(parent_node.left), self.height_determiner(parent_node.right))
        left_child.height = 1 + max(self.height_determiner(left_child.left), self.height_determiner(left_child.right))

        return left_child

    def height_difference_between_left_and_right_subtrees(self, node):

        if not node:
            return 0

        return self.height_determiner(node.left) - self.height_determiner(node.right)

    def in_order_traversal(self, node):
        if node is None:
            return []
        result = []
        result.extend(self.in_order_traversal(node.left))
        result.append(node.value)
        result.extend(self.in_order_traversal(node.right))
        return result


