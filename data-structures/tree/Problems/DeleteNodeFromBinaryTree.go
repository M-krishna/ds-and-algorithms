// Delete a node with a specific key in binary tree
package main

import "fmt"

type Node struct {
	value       int
	left, right *Node
}

type BinaryTree struct {
	root *Node
}

type Queue struct {
	front, rear, size, capacity int
	data                        []*Node
}

func NewQueue(capacity int) *Queue {
	return &Queue{
		size:     0,
		capacity: capacity,
		front:    0,
		rear:     capacity - 1,
		data:     make([]*Node, capacity),
	}
}

func NewBinaryTree(rootValue int) *BinaryTree {
	node := &Node{value: rootValue}
	return &BinaryTree{
		root: node,
	}
}

func NewNode(nodeValue int) *Node {
	return &Node{
		value: nodeValue,
	}
}

func (q *Queue) IsFull() bool {
	return q.size == q.capacity
}

func (q *Queue) IsEmpty() bool {
	return q.size == 0
}

func (q *Queue) Enqueue(node *Node) {
	if q.IsFull() {
		fmt.Println("Queue is Full!")
		return
	}
	q.rear = (q.rear + 1) % q.capacity
	q.data[q.rear] = node
	q.size++
}

func (q *Queue) Dequeue() *Node {
	if q.IsEmpty() {
		fmt.Println("Queue is empty!")
		return nil
	}
	data := q.data[q.front]
	q.front = (q.front + 1) % q.capacity
	q.size--
	return data
}

func (b *BinaryTree) PrintLevelOrderTraversal() {
	// create an empty queue
	q := NewQueue(5)

	// create a temp node and assign the node to it
	temp_node := b.root

	for temp_node != nil {
		// print the value
		fmt.Printf("%d ", temp_node.value)

		if temp_node.left != nil {
			q.Enqueue(temp_node.left)
		}
		if temp_node.right != nil {
			q.Enqueue(temp_node.right)
		}

		temp_node = q.Dequeue()
	}
}

// Using the same LOT Queue fashion to delete the node
func (b *BinaryTree) DeleteDeepest(nodeToBeDeleted *Node) {
	// create an empty queue
	q := NewQueue(5)

	// enqueue the root node
	q.Enqueue(b.root)

	// create a temp_node variable
	var temp_node *Node = nil

	// continue until the queue is empty.
	for !q.IsEmpty() {
		temp_node = q.Dequeue()
		if temp_node.value == nodeToBeDeleted.value {
			temp_node = nil
			return
		}

		if temp_node.left != nil {
			if temp_node.left.value == nodeToBeDeleted.value {
				temp_node.left = nil
				return
			} else {
				q.Enqueue(temp_node.left)
			}
		}

		if temp_node.right != nil {
			if temp_node.right.value == nodeToBeDeleted.value {
				temp_node.right = nil
				return
			} else {
				q.Enqueue(temp_node.right)
			}
		}
	}
}

func (b *BinaryTree) DeleteKey(key int) {
	// create an empty queue
	q := NewQueue(5)

	// enqueue the root node
	q.Enqueue(b.root)

	// create a temp_node variable and key_node variable to store the node
	var temp_node *Node = nil
	var key_node *Node = nil

	// Continue until the queue is empty.
	for !q.IsEmpty() {
		temp_node = q.Dequeue()
		if temp_node.value == key {
			key_node = temp_node
		}
		if temp_node.left != nil {
			q.Enqueue(temp_node.left)
		}
		if temp_node.right != nil {
			q.Enqueue(temp_node.right)
		}
	}
	// If we found the key_node replace the value with temp_node
	if key_node != nil {
		temp_node_data := temp_node.value
		b.DeleteDeepest(temp_node)
		key_node.value = temp_node_data
	}
}

func main() {
	tree := NewBinaryTree(1)
	tree.root.left = NewNode(2)
	tree.root.right = NewNode(3)
	tree.root.left.left = NewNode(4)
	tree.root.left.right = NewNode(5)

	tree.PrintLevelOrderTraversal()

	key := 3
	tree.DeleteKey(key)
	tree.PrintLevelOrderTraversal()
}
