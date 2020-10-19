package main

import "fmt"

type Node struct{
	value int
	next *Node
}

type List struct{
	head *Node
}

func (l *List) insertNode (newNode *Node){
	if l.head == nil {
		l.head = newNode
	} else {
		currentNode := l.head
		for currentNode.next != nil {
			currentNode = currentNode.next
		}
		currentNode.next = newNode
	}
}

func (l *List) removeFirstNode() {
	list := l.head
	if list != nil {
		l.head = l.head.next
		return	
	}
}

func (l *List) deleteNode (node *Node){
	temp := l.head
	if temp != nil {
		if temp == node {
			l.head = temp.next
			temp = nil
			return
		}
	}

	var prev *Node

	for temp != nil {
		if temp == node {
			break
		}
		prev = temp
		temp = temp.next
	}

	prev.next = temp.next
	temp = nil
}

func (l *List) display() {
	list := l.head
	for list != nil {
		fmt.Printf("%v -> ", list.value)
		list = list.next
	}
	fmt.Println()
}

// Iterative method
func (l *List) IterativeReverse() {
	var previousNode *Node = nil
	var currentNode *Node = l.head
	var nextNode *Node = nil

	for currentNode != nil{
		nextNode = currentNode.next
		currentNode.next = previousNode
		previousNode = currentNode
		currentNode = nextNode
	}
	l.head = previousNode
}

// Sort the LinkedList using bubble sort
// Time Complexity: O(n^2)
// Space Complexity: O(1)
func (l *List) bubbleSort() {
	current := l.head
	var index *Node = nil

	for current != nil {
		index = current.next
		for index != nil {
			if current.value > index.value {
				current.value, index.value = index.value, current.value
			}
			index = index.next
		}
		current = current.next
	}
}

func main(){
	items := &List{}
	node1 := Node{value: 10,}
	node2 := Node{value: 2,}
	node3 := Node{value: 33,}
	node4 := Node{value: 4,}

	items.insertNode(&node1)
	items.insertNode(&node2)
	items.insertNode(&node3)
	items.insertNode(&node4)

	items.display()

	// Removing the first node.
	// items.removeFirstNode()

	// items.display()

	// // Removing the first node.
	// items.removeFirstNode()

	// items.display()

	// Delete a specific node.
	// items.deleteNode(&node1)
	items.IterativeReverse()
	items.display()
	items.bubbleSort()
	items.display()
}