// Level order traversal using queue
// Time Complexity: O(n) where n is the number of nodes in the binary tree
// Space Complexity: O(n) where n is the number of nodes in the binary tree

package main

import "fmt"

type Node struct {
	data int
	left, right *Node
}

type Queue struct {
	front, rear int
	data []*Node
	capacity int
	size int
}

func NewNode(data int) *Node {
	return &Node{
		data: data,
	}
}

func NewQueue(capacity int) *Queue {
	return &Queue{
		front: 0,
		rear: capacity - 1,
		capacity: capacity,
		size: 0,
		data: make([]*Node, capacity),
	}
}

func (q *Queue) IsEmpty() bool {
	return q.size == 0
}

func (q *Queue) IsFull() bool {
	return q.size == q.capacity
}

func (q *Queue) Enqueue(node *Node) {
	if q.IsFull() {
		fmt.Println("Queue overflow!")
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


func printLevelOrderTraversal(node *Node) {
	// create an empty queue
	q := NewQueue(5) // 5 is the capacity of the queue

	// create a temp_node and assign the value of root node
	temp_node := node

	for temp_node != nil {
		// print the value of the temp node
		fmt.Printf("%d ", temp_node.data)

		// check if the node has left and right children
		// if its there then push it to the queue
		if temp_node.left != nil {
			q.Enqueue(temp_node.left)
		}
		if temp_node.right != nil {
			q.Enqueue(temp_node.right)
		}

		// Dequeue the queue and assign the value to temp_node
		temp_node = q.Dequeue()
	}
}

func main() {
	root := NewNode(10)
	root.left = NewNode(20)
	root.right = NewNode(30)
	root.left.left = NewNode(40)
	root.left.right = NewNode(50)
	root.right.left = NewNode(60)
	root.right.right = NewNode(70)

	printLevelOrderTraversal(root)
}