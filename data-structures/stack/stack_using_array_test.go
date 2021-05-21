package stack

import (
	"testing"
)

func TestStackUsingArray(t *testing.T) {
	// create an empty stack
	s := NewStack()
	if !s.IsEmpty() {
		t.Error("It is empty stack!")
	} else {
		t.Log("Sucess!")
	}
}
