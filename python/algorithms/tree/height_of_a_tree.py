'''
The height of a binary tree is the number of edges between the tree's root and its furthest leaf. 
'''

from __future__ import annotations

class Node:
    def __init__(self, data: int, left: Node = None, right: Node = None) -> None:
        self.data = data
        self.left = left
        self.right = right

def height(root: Node) -> int:
    if not root:
        return 0

    leftSubTreeHeight = height(root.left)
    rightSubTreeHeight = height(root.right)
    return max(leftSubTreeHeight, rightSubTreeHeight) + 1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    print(height(root))