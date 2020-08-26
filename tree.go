package main

import "fmt"

type Node struct {
	data int
	left, right *Node
}

func Preorder(node *Node) {
	if node == nil {
		return
	}
	fmt.Println(node.data)
	Preorder(node.left)
	Preorder(node.right)
}

func Inorder(node *Node) {
	if node == nil {
		return
	}

	Inorder(node.left)
	fmt.Println(node.data)
	Inorder(node.right)
}

func Postorder(node *Node) {
	if node == nil {
		return
	}

	Postorder(node.left)
	Postorder(node.right)
	fmt.Println(node.data)
}

func main() {
	root := Node{data: 1,}
	root.left = &Node{data: 2,}
	root.right = &Node{data: 3,}
	root.left.left = &Node{data: 4,}
	root.left.right = &Node{data: 5,}
	root.right.left = &Node{data: 6,}
	root.right.right = &Node{data: 7,}
	fmt.Println("Inorder")
	Inorder(&root)
	fmt.Println("Preorder")
	Preorder(&root)
	fmt.Println("Postorder")
	Postorder(&root)
}