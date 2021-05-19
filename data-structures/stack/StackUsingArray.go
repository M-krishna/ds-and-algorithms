// Stack implemented using an array
package main

import "fmt"

type Stack struct {
	array []int
}

func newStack() *Stack{
	return &Stack{
		array: make([]int, 0),
	}
}

func (s *Stack) IsEmpty() bool {
	return len(s.array) == 0
}

func (s *Stack) Push(d int) {
	s.array = append(s.array, d)
}

func (s *Stack) Pop() {
	if s.IsEmpty() {
		fmt.Println("Stack is empty")
	}
	length := len(s.array)
	s.array = s.array[:length-1]
}

func (s *Stack) Peek() {
	if s.IsEmpty() {
		fmt.Println("Stack is empty")
		return
	}
	length := len(s.array)
	fmt.Println(s.array[length-1])
}

func main() {
	s := newStack()
	s.Push(1)
	s.Push(2)
	fmt.Println(s.IsEmpty())
	s.Push(3)
	s.Peek()
	s.Pop()
	s.Peek()
	s.Pop()
	s.Peek()
	s.Pop()
	s.Peek()
}