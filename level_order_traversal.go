// Level order traversal of a binary tree.
// To do LOT we have first find the height of the binary tree.
// we can find the height by going from root node to deepest leaf node (recursively)

package main

import "fmt"

type Node struct {
	data int
	left *Node
	right *Node
}

func NewTree(data int) *Node {
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
	root := NewTree(10)
	root.left = &Node{data: 20,}
	root.right = &Node{data: 30,}
	root.left.left = &Node{data: 40,}
	root.left.right = &Node{data: 50,}
	
	fmt.Println(treeHeight(root))
	printLevelOrderTraversal(root)
}