// Check if a binary tree is a valid BST.
package main

import (
	"fmt"
)

var (
	INT_MIN int = -4294967296
	INT_MAX int = 4294967296
)

type Node struct {
	value int
	left, right *Node
}


func NewNode(value int) *Node {
	return &Node{
		value: value,
	}
}

// Using Min, Max value to check valid BST
// Time Complexity: O(n)
// Space Complexity: O(h), where h is the height of the tree.
func isValidBST(root *Node, min, max int) bool {
	if root == nil {
		return true
	} else if root.value <= min || root.value >= max {
		return false
	} else {
		return isValidBST(root.left, min, root.value) && isValidBST(root.right, root.value, max)
	}
}

func main() {
	root := NewNode(16)
	root.left = NewNode(8)
	root.right = NewNode(22)
	root.left.left = NewNode(3)
	root.left.right = NewNode(11)
	root.left.left.left = NewNode(1)
	root.left.left.right = NewNode(6)

	fmt.Println(isValidBST(root, INT_MIN, INT_MAX))
}