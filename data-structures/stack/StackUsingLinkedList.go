// Implementing stack using LinkedList

package main

import "fmt"

type StackNode struct {
	data int
	next *StackNode
}

type Stack struct {
	root *StackNode
}


func (s *Stack) IsEmpty() bool{
	if s.root == nil {
		return true
	}
	return false
}


func (s *Stack) Push(d int) {
	newStackNode := StackNode{data: d,}
	newStackNode.next = s.root
	s.root = &newStackNode
}

func (s *Stack) Pop() {
	if s.IsEmpty() {
		fmt.Println("The Stack is empty")
		return
	}
	rootNode := s.root
	s.root = s.root.next
	popped := rootNode.data
	fmt.Printf("%d Popped from stack\n", popped)
}

func (s *Stack) Peek(){
	if s.IsEmpty() {
		fmt.Println("The stack is empty")
		return
	}
	fmt.Println(s.root.data)
}

func main () {
	s := Stack{}
	s.Push(1)
	s.Push(2)
	s.Push(3)
	s.Push(4)
	s.Push(5)
	s.Peek()
	s.Pop()
	s.Peek()
	fmt.Println(s.IsEmpty())
}