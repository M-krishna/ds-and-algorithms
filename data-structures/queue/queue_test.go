package queue

import "testing"

func TestQueueIsEmpty(t *testing.T) {
	q := NewQueue(1)
	if !q.IsEmpty() {
		t.Error("Queue is empty!")
	} else {
		t.Log("Success!")
	}

}

func TestQueueIsNotEmpty(t *testing.T) {
	q := NewQueue(2)
	q.Enqueue("1")
	q.Enqueue("2")
	if q.IsEmpty() {
		t.Error("Queue is not empty!")
	} else {
		t.Log("Success!")
	}
}

func TestQueueIsFull(t *testing.T) {
	q := NewQueue(2)
	q.Enqueue("1")
	q.Enqueue("2")
	if !q.IsFull() {
		t.Error("Queue is not full!")
	} else {
		t.Log("Success!")
	}
}

func TestQueueIsNotFull(t *testing.T) {
	q := NewQueue(2)
	q.Enqueue("1")
	if q.IsFull() {
		t.Error("Queue is full!")
	} else {
		t.Log("Success!")
	}
}

func TestQueuePeek(t *testing.T) {
	q := NewQueue(2)
	q.Enqueue("1")
	q.Enqueue("2")
	expected_peek_value := "1"
	if val, err := q.Peek(); err != nil {
		t.Error(err)
	} else if val != expected_peek_value {
		t.Errorf("Expected value %v, got %v", expected_peek_value, val)
	} else {
		t.Log("Success!")
	}
}

// TODO: Add in more parameterized enqueue test
func TestEnqueue(t *testing.T) {
	q := NewQueue(1)
	if err := q.Enqueue("1"); err != nil {
		t.Error(err)
	} else {
		t.Log("Success!")
	}
}

func TestDequeue(t *testing.T) {
	q := NewQueue(2)
	q.Enqueue("1")
	q.Enqueue("2")
	expected_dequeue_val := "1"
	if val, err := q.Dequeue(); err != nil {
		t.Error(err)
	} else if val != expected_dequeue_val {
		t.Errorf("Expected value %v, got %v", expected_dequeue_val, val)
	} else {
		t.Log("Success!")
	}
}
