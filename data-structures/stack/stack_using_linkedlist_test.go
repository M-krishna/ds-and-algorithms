package stack

import "testing"

func TestLNstackIsEmpty(t *testing.T) {
	s := NewStackUsingLinkedList()
	if !s.IsEmpty() {
		t.Error("Stack is Empty!")
	} else {
		t.Log("Success!")
	}
}

func TestLNStackNotEmpty(t *testing.T) {
	s := NewStackUsingLinkedList()
	s.Push("1")
	s.Push("2")
	if s.IsEmpty() {
		t.Error("Stack is not empty!")
	} else {
		t.Log("Success!")
	}
}

func TestLNStackPeek(t *testing.T) {
	s := NewStackUsingLinkedList()
	s.Push("1")
	s.Push("2")
	expected_value := "2"
	if val, err := s.Peek(); err != nil {
		t.Error(err)
	} else if val != expected_value {
		t.Errorf("Expected value %s, got %s", expected_value, val)
	} else {
		t.Log("Success!")
	}
}

func TestLNStackPop(t *testing.T) {
	s := NewStackUsingLinkedList()
	s.Push("1")
	s.Push("2")
	expected_value := "2"
	if val, err := s.Pop(); err != nil {
		t.Error(err)
	} else if val != expected_value {
		t.Errorf("Expected value %s, got %s", expected_value, val)
	} else {
		t.Log("Success!")
	}
}

/*
	TODO: Add test for push method
*/
