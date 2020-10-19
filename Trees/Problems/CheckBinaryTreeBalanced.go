// Program to check if a binary tree is balanced or not.
// A binary tree is balanced based on few conditions
// If the root node is null then it is balanced
// If the root node is not null then the following condition applies
//	* the difference between the height of the left subtree and the height of
//	  the right subtree is among the values -1, 0, 1.
//	* the left subtree is balanced.
//	* the right subtree is balanced.

package main

import (
	"fmt"
	"math"
)

type Node struct {
	value float64
	left, right *Node
}

func NewNode(value float64) *Node {
	return &Node{
		value: value,
	}
}

func height(root *Node) float64 {
	if root == nil {
		return 0
	}

	return (math.Max(height(root.left), height(root.right))) + 1
}

// Time Complexity: O(n^2) worst case occurs in case skewed tree
// Space Complexity: O(h)
func isBalanced(node *Node) bool {
	if node == nil {
		return true
	}

	lh := height(node.left)
	rh := height(node.right)

	if math.Abs(lh - rh) <= 1 && isBalanced(node.left) && isBalanced(node.right) {
		return true
	}
	return false
}

func main() {
	root := NewNode(1)
	root.left = NewNode(2)
	root.right = NewNode(3)
	root.left.left = NewNode(4)
	root.left.right = NewNode(5)
	root.left.right.left = NewNode(6)

	fmt.Println(isBalanced(root))
}