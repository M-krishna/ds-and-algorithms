package main

import (
	"fmt"
)

type Node struct {
	data int
	next *Node
}

type List struct {
	head *Node
}

func createList() *List {
	return &List{}
}

func (l *List) insertAtBeginning(data int) {
	node := &Node{data: data}
	if l.head == nil {
		l.head = node
		node.next = l.head
	} else {
		currentNode := l.head
		for currentNode.next != l.head {
			currentNode = currentNode.next
		}
		node.next = currentNode.next
		currentNode.next = node
		l.head = node
	}
	fmt.Println(l.head.data, l.head.next.data)
}

func (l *List) insertAtLast(data int) {
	node := &Node{data: data}
	if l.head == nil {
		l.head = node
		node.next = l.head
	} else {
		var currentNode *Node = l.head
		for currentNode.next != l.head {
			currentNode = currentNode.next
		}
		currentNode.next = node
		node.next = l.head
	}
}

func (l *List) displayItems() {
	var currentNode *Node = l.head
	for currentNode.next != l.head {
		fmt.Printf("[%v] -> ", currentNode.data)
		currentNode = currentNode.next
	}
	// fmt.Printf("[%v] -> [%v]", l.head.data, l.head.next.data)
	fmt.Println()
}

func main() {
	items := createList()
	items.insertAtBeginning(1)
	items.insertAtBeginning(2)
	// items.insertAtLast(2)
	// items.insertAtLast(3)
	// items.insertAtLast(4)
	// items.insertAtLast(5)
	// items.insertAtLast(6)
	items.displayItems()
}
