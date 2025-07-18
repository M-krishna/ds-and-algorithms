"""
Print the top view of a binary tree
"""


from __future__ import annotations

class Node:
    def __init__(self, data: int, left: Node = None, right: Node = None) -> None:
        self.data = data
        self.left = left
        self.right = right


def top_view(root):
    left = root.left
    right = root.right

    left_data = []
    while left is not None:
        left_data.append(left.data)
        left = left.left

    right_data = []
    while right is not None:
       right_data.append(right.data) 
       right = right.right

    print(left_data)
    print(right_data)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.right = Node(7)

    print(top_view(root))