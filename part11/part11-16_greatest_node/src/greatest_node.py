class Node:
    def __init__(self, value, left_child: "Node" = None, right_child: "Node" = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def greatest_node(root: Node):
    current_max = root.value

    if root.left_child:
        left_max = greatest_node(root.left_child)
        current_max = max(current_max, left_max)

    if root.right_child:
        right_max = greatest_node(root.right_child)
        current_max = max(current_max, right_max)

    return current_max
