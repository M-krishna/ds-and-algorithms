

from __future__ import annotations

"""Depth first search"""

"""
In DFS, we have three things
* Inorder (LNR) -> Left Node Right
* Preorder (NLR) -> Node Left Right
* Postorder (LRN) -> Left Right Node

The above three things helps us with traversing a tree.

We'll try to implement these functions both recursively and iteratively
"""

class Node:
    def __init__(self, data: int, left: Node = None, right: Node = None):
        self.data = data
        self.left = left
        self.right = right



# Recursive version of inorder function
def inorder_rec(root):
    if root is None:
        return
    inorder_rec(root.left)
    print(root.data, end=" ")
    inorder_rec(root.right)

# Iterative version of inorder function
def inorder_iter(root: Node):
    stack = []
    curr_node: Node = root

    while curr_node is not None or len(stack) != 0:

        while curr_node is not None:
            stack.append(curr_node)
            curr_node = curr_node.left

        curr_node = stack.pop()
        print(curr_node.data, end=" ")

        curr_node = curr_node.right


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    inorder_rec(root)
    print()
    inorder_iter(root)