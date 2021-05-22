package stack

import (
	"testing"
)

func TestStackIsEmpty(t *testing.T) {
	// create an empty stack
	s := NewStack()
	if !s.IsEmpty() {
		t.Error("Stack is empty!")
	} else {
		t.Log("Success!")
	}
}

func TestStackNotEmpty(t *testing.T) {
	s := NewStack()
	s.Push("1")
	s.Push("2")
	if !s.IsEmpty() {
		t.Log("Success!")
	} else {
		t.Error("Stack is not empty!")
	}
}

func TestStackPeek(t *testing.T) {
	s := NewStack()
	s.Push("1")
	s.Push("2")
	if _, err := s.Peek(); err != nil {
		t.Error(err)
	} else {
		t.Log("Success!")
	}
}

func TestStackPop(t *testing.T) {
	s := NewStack()
	s.Push("1")
	s.Push("2")
	s.Push("3")
	if _, err := s.Pop(); err != nil {
		t.Error(err)
	} else {
		t.Log("Success!")
	}
}

/*
	TODO: Add test for Push method
	Since the stack is not created using fixed length we can able to push n number of items
*/
