// Level order traversal of a binary tree.
// To do LOT we have first find the height of the binary tree.
// we can find the height by going from root node to deepest leaf node (recursively)

// Time Complexity O(n^2) for worst case. In a skewed tree its O(log n)
// Space complxity O(n).

package main

import "fmt"

type Node struct {
	data int
	left, right *Node
}

func NewNode(data int) *Node {
	return &Node{
		data: data,
	}
}

func treeHeight(node *Node) int{
	if node == nil {
		return 0
	}

	left_subtree := treeHeight(node.left)
	right_subtree := treeHeight(node.right)

	if left_subtree > right_subtree {
		return left_subtree + 1
	} else {
		return right_subtree + 1
	}
}

func printLevelOrderTraversal(root *Node) {
	h := treeHeight(root)
	for i := 0; i < h; i++ {
		levelOrderTraversal(root, i)
	}
}

func levelOrderTraversal(node *Node, level int) {
	if node == nil {
		return
	}

	if level == 0 {
		fmt.Printf("%d ", node.data)
	} else {
		levelOrderTraversal(node.left, level - 1)
		levelOrderTraversal(node.right, level - 1)
	}
}


func main() {
	root := NewNode(10)
	root.left = NewNode(20)
	root.right = NewNode(30)
	root.left.left = NewNode(40)
	root.left.right = NewNode(50)
	
	fmt.Println(treeHeight(root))
	printLevelOrderTraversal(root)
}