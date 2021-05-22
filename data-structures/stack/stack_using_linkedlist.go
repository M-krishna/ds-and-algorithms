// Implementing stack using LinkedList

package stack

import (
	"errors"
)

type StackUsingLinkedList interface {
	IsEmpty() bool
	Push(string)
	Pop() (string, error)
	Peek() (string, error)
}

type StackNode struct {
	data string
	next *StackNode
}

type stackUsingLinkedList struct {
	root *StackNode
}

func NewStackUsingLinkedList() StackUsingLinkedList {
	return &stackUsingLinkedList{}
}

func (s *stackUsingLinkedList) IsEmpty() bool {
	if s.root == nil {
		return true
	}
	return false
}

func (s *stackUsingLinkedList) Push(data string) {
	// creating the new stack node
	newStackNode := StackNode{data: data}
	newStackNode.next = s.root
	s.root = &newStackNode
}

func (s *stackUsingLinkedList) Pop() (string, error) {
	if s.IsEmpty() {
		return "", errors.New("Stack is empty!")
	}
	rootNode := s.root
	s.root = s.root.next
	popped := rootNode.data
	return popped, nil
}

func (s *stackUsingLinkedList) Peek() (string, error) {
	if s.IsEmpty() {
		return "", errors.New("Stack is empty!")
	}
	return s.root.data, nil
}
