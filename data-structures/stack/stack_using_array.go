// Stack implemented using an array
package stack

import (
	"errors"
)

type Stack interface {
	IsEmpty() bool
	Push(string)
	Pop() (string, error)
	Peek() (string, error)
}

type stack struct {
	arr []string
}

func NewStack() Stack {
	return &stack{
		arr: make([]string, 0),
	}
}

func (s *stack) IsEmpty() bool {
	return len(s.arr) == 0
}

func (s *stack) Push(d string) {
	s.arr = append(s.arr, d)
}

func (s *stack) Pop() (string, error) {
	if s.IsEmpty() {
		return "", errors.New("Stack is Empty!")
	}
	length := len(s.arr)
	popped_element := s.arr[length-1]
	s.arr = s.arr[:length-1]
	return popped_element, nil
}

func (s *stack) Peek() (string, error) {
	if s.IsEmpty() {
		return "", errors.New("Stack is empty!")
	}
	length := len(s.arr)
	return s.arr[length-1], nil
}
