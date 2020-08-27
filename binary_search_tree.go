// Recursive Solutions

package main

import "fmt"

type Node struct {
	data int
	left, right *Node
}

type BinaryTree struct {
	root *Node
}

func (t *BinaryTree) insert(data int) *BinaryTree {
	if t.root == nil {
		t.root = &Node{data: data,}
	} else {
		t.root.insert(data)
	}
	return t
}

func (n *Node) insert(data int) {
	if n == nil {
		return
	} else if data <= n.data {
		if n.left == nil {
			n.left = &Node{data: data,}
		} else {
			n.left.insert(data)
		}
	} else {
		if n.right == nil {
			n.right = &Node{data: data,}
		} else {
			n.right.insert(data)
		}
	}
}

func (t *BinaryTree) Preorder(node *Node) {
	if node == nil {
		return
	}

	fmt.Println(node.data)
	t.Preorder(node.left)
	t.Preorder(node.right)
}

func (t *BinaryTree) Inorder(node *Node) {
	if node == nil {
		return
	}

	t.Inorder(node.left)
	fmt.Println(node.data)
	t.Inorder(node.right)
}

func (t *BinaryTree) Postorder(node *Node) {
	if node == nil {
		return
	}

	t.Postorder(node.left)
	t.Postorder(node.right)
	fmt.Println(node.data)
}

// Iterative Search of a node
func (t *BinaryTree) Search(data int) {
	currentNode := t.root

	for currentNode != nil {
		if currentNode.data == data {
			fmt.Println("Data found ", currentNode.data)
			return
		} else if currentNode.data > data {
			currentNode = currentNode.left
		} else {
			currentNode = currentNode.right
		}
	}
	fmt.Printf("%d not found!\n", data)
}

// Get the inorder successor value of the node
func (t *BinaryTree) MinValue(node *Node) *Node {
	if node == nil {
		return nil
	}
	currentNode := node

	for currentNode != nil {
		currentNode = currentNode.left
	}
	return currentNode
}

// Deleting a node (Recursive solution)
func (t *BinaryTree) Delete(root *Node, data int) *Node {
	if root == nil {
		return nil
	}

	if root.data > data {
		root.left = t.Delete(root.left, data)
	} else if root.data < data {
		root.right = t.Delete(root.right, data)
	} else {
		// If the node has only one or no child
		if root.left == nil {
			return root.right
		} else if root.right == nil {
			return root.left
		}

		// If the node has 2 child, get the inorder successor of the node
		root.data = t.MinValue(root.right).data

		// Now delete the inorder successor
		root.right = t.Delete(root.right, root.data)
	}
	return root
}

func main() {
	tree := &BinaryTree{}
	tree.insert(100).
		insert(-20).
        insert(-50).
        insert(-15).
        insert(-60).
        insert(50).
        insert(60).
        insert(55).
        insert(85).
        insert(15).
        insert(5).
        insert(-10)

    fmt.Println("Preorder")
    tree.Preorder(tree.root)

    fmt.Println("Inorder")
    tree.Inorder(tree.root)

    fmt.Println("Postorder")
    tree.Postorder(tree.root)

    fmt.Println("Search")
    tree.Search(55)

    fmt.Println("Delete")
    tree.Delete(tree.root, 55)

    fmt.Println("Inorder Traversal after deletion")
    tree.Inorder(tree.root)
}