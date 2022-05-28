# Basic Tree implementation

from __future__ import annotations


class Node:
    def __init__(self, data: str, left: Node | None = None, right: Node | None = None):
        self.data: str = data
        self.left: Node | None = left
        self.right: Node | None = right

    # left, node, right
    @classmethod
    def in_order(cls, node: Node | None):
        if node:
            cls.in_order(node.left)
            print(node.data, end=" ")
            cls.in_order(node.right)

    # node, left, right
    @classmethod
    def pre_order(cls, node: Node | None):
        if node:
            print(node.data, end=" ")
            cls.pre_order(node.left)
            cls.pre_order(node.right)

    # left, right, node
    @classmethod
    def post_order(cls, node: Node | None):
        if node:
            cls.post_order(node.left)
            cls.post_order(node.right)
            print(node.data, end=" ")


if __name__ == "__main__":
    root = Node("1")
    root.left = Node("2")
    root.right = Node("3")

    root.left.left = Node("4")
    root.left.right = Node("5")

    root.right.left = Node("6")
    root.right.right = Node("7")

    """
	    1
	   2 3
	 4 5 6 7
	"""

    # Inorder traversal
    print("Inorder traversal")
    Node.in_order(root)  # 4 2 5 1 6 3 7
    print()  # new line

    # Preorder traversal
    print("Preorder traversal")
    Node.pre_order(root)  # 1 2 4 5 3 6 7
    print()  # new line

    # Postorder traversal
    print("Postorder traversal")
    Node.post_order(root)  # 4 5 2 6 7 3 1
    print()  # new line
