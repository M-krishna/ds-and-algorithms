from __future__ import annotations
from typing import List


"""
Depth First Search

There are 3 types of DFS:
* In-order (Left -> Node -> Right)
* Pre-order (Node -> Left -> Right)
* Post-order (Left -> Right -> Node)

Given the below tree, print the inorder, preorder and postorder

       1
      / \
     2   3
    / \ / \
   4  5 6  7
"""


class Node:
    def __init__(self, data: int, left: Node = None, right: Node = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.data)


# Recursive version of Inorder traversal
def inorder_rec(root: Node):
    if root is None: return

    inorder_rec(root.left)
    print(root.data, end=" ")
    inorder_rec(root.right)

# Iterative version of Inorder traversal
def inorder_iter(root: Node):
    stack: List[Node] = []
    curr_node: Node = root
    
    while curr_node is not None or len(stack) != 0:

        while curr_node is not None:
            stack.append(curr_node)
            curr_node = curr_node.left

        curr_node = stack.pop()
        print(curr_node.data, end=" ")

        curr_node = curr_node.right

# Recursive version of Preorder traversal
def preorder_rec(root: Node):
    if root is None: return

    print(root.data, end=" ")
    preorder_rec(root.left)
    preorder_rec(root.right)

# Iterative version of Preorder traversal
def preorder_iter(root: Node):
    if root is None: return

    stack: List[Node] = []
    stack.append(root)

    while stack:
        curr_node: Node = stack.pop()
        print(curr_node.data, end=" ")

        if curr_node.right:
            stack.append(curr_node.right)

        if curr_node.left:
            stack.append(curr_node.left)
    
# Recursive version of Postorder traversal
def postorder_rec(root: Node):
    if root is None: return

    postorder_rec(root.left)
    postorder_rec(root.right)
    print(root.data, end=" ")

# Iterative version of Postorder traversal
def postorder_iter1(root: Node):
    if root is None: return

    stack1: List[Node] = []
    stack2: List[Node] = []

    stack1.append(root)
    while len(stack1) != 0:
        curr_node = stack1.pop()
        stack2.append(curr_node)

        if curr_node.left:
            stack1.append(curr_node.left)
        
        if curr_node.right:
            stack1.append(curr_node.right)
    
    while len(stack2) != 0:
        curr_node = stack2.pop()
        print(curr_node.data, end=" ")

# Iterative version of Postorder traversal 2
def postorder_iter2(root: Node):
    if root is None: return

    stack: List[Node] = []
    lastVisitedNode: Node = None

    while True:
        curr_node: Node = root
        while curr_node is not None:
            stack.append(curr_node)
            curr_node = curr_node.left

        if not stack:
            break

        curr_node = stack[-1]
        if curr_node.right is None or curr_node.right == lastVisitedNode:
            print(curr_node.data, end=" ")
            lastVisitedNode = stack.pop()
            curr_node = None
        else:
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
    print()
    preorder_rec(root)
    print()
    preorder_iter(root)
    print()
    postorder_rec(root)
    print()
    postorder_iter1(root)
    print()
    postorder_iter2(root)