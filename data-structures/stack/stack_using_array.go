// Stack implemented using an array
package stack

import "fmt"

type Stack interface {
	IsEmpty() bool
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

func (s *stack) Pop() {
	if s.IsEmpty() {
		fmt.Println("Stack is empty")
	}
	length := len(s.arr)
	s.arr = s.arr[:length-1]
}

func (s *stack) Peek() {
	if s.IsEmpty() {
		fmt.Println("Stack is empty")
		return
	}
	length := len(s.arr)
	fmt.Println(s.arr[length-1])
}
