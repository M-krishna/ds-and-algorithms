package main

import ("fmt")

type Node struct {
	data int
	prev *Node
	next *Node
}

type List struct {
	head *Node
	tail *Node
}

func createList () *List {
	return &List{}
}

func (l *List) insertNewNodeAtLast(data int) {
	// create a node
	node := &Node{data: data,}

	if l.head == nil {
		l.head = node
	} else {
		currentNode := l.tail
		currentNode.next = node
		node.prev = l.tail
	}
	l.tail = node
}

func (l *List) insertNewNodeAtFirst(data int) {
	node := &Node{data: data,}
	if l.head == nil {
		l.head = node
	} else {
		currentNode := l.head
		l.head = node
		l.head.next = currentNode
		currentNode.prev = l.head
	}
}

func (l *List) addNodeAfterAGivenNode(prevNode int, data int) {
	node := &Node{data: data,}
	if l.head == nil {
		l.head = node
	} else if l.head.data == prevNode {
		currentNode := l.head
		node.prev = currentNode
		node.next = currentNode.next
		currentNode.next.prev = node
		currentNode.next = node
	} else if l.tail.data == prevNode {
		currentNode := l.tail
		node.prev = currentNode
		currentNode.next = node
		l.tail = node
	} else {
		currentNode := l.head
		for currentNode != nil {
			if(currentNode.data == prevNode) {
				temp := currentNode
				node.prev = temp
				node.next = temp.next
				temp.next = node
				break
			}
			currentNode = currentNode.next
		}
	}
}

func (l *List) addNodeBeforeAGivenNode(nextNode int, data int) {
	node := &Node{data: data,}
	if l.head == nil {
		return
	} else if l.head.data == nextNode {
		currentNode := l.head
		node.next = currentNode
		currentNode.prev = node
		l.head = node
		return
	} else if l.tail.data == nextNode {
		currentNode := l.tail
		node.prev = currentNode.prev
		currentNode.prev.next = node
		currentNode.prev = node
		node.next = currentNode
		return
	} else {
		currentNode := l.head
		for currentNode != nil {
			if(currentNode.data == nextNode) {
				node.prev = currentNode.prev
				currentNode.prev.next = node
				currentNode.prev = node
				node.next = currentNode
				break
			}
			currentNode = currentNode.next
		}
	}
}

func (l *List) reverseDll() {
	list := l.tail
	for list != nil {
		fmt.Printf("[%v] -> ", list.data)
		list = list.prev
	}
}

func (l *List) getTheFirstNode() {
	fmt.Printf("[%v]", l.head.data)
}

func (l *List) getTheLastNode() {
	fmt.Printf("[%v]", l.tail.data)
}

func (l *List) displayItems() {
	list := l.head
	for list != nil {
		fmt.Printf("[%v] -> ", list.data)
		list = list.next
	}
}

func main() {
	// create a list
	items := createList()
	items.insertNewNodeAtLast(1)
	items.insertNewNodeAtLast(2)
	items.insertNewNodeAtFirst(3)
	items.insertNewNodeAtFirst(4)
	items.insertNewNodeAtFirst(5)
	items.displayItems()
	fmt.Println()
	items.addNodeAfterAGivenNode(5, 50)
	items.displayItems()
	fmt.Println()
	items.addNodeAfterAGivenNode(2, 20)
	items.displayItems()
	fmt.Println()
	items.addNodeBeforeAGivenNode(5, 55)
	items.displayItems()
	fmt.Println()
	items.addNodeBeforeAGivenNode(20, 200)
	items.displayItems()
	fmt.Println()
	items.addNodeBeforeAGivenNode(3, 30)
	items.displayItems()
	fmt.Println()
	items.getTheFirstNode()
	fmt.Println()
	items.getTheLastNode()
	fmt.Println()
	items.reverseDll()
}