// Implementation of Queue using 1D Array

package queue

import "errors"

type Queue interface {
	IsEmpty() bool
	IsFull() bool
	Peek() (string, error)
	Enqueue(string) error
	Dequeue() (string, error)
}

type queue struct {
	front    int
	rear     int
	arr      []string
	capacity int
	size     int
}

func NewQueue(capacity int) Queue {
	return &queue{
		front:    0,
		rear:     capacity - 1,
		arr:      make([]string, capacity),
		capacity: capacity,
		size:     0,
	}
}

func (q *queue) IsEmpty() bool {
	return q.size == 0
}

func (q *queue) IsFull() bool {
	return q.size == q.capacity
}

func (q *queue) Peek() (string, error) {
	if q.IsEmpty() {
		return "", errors.New("Queue is empty!")
	}
	return q.arr[q.front], nil
}

func (q *queue) Enqueue(data string) error {
	if q.IsFull() {
		return errors.New("Queue overflow!")
	}
	q.rear = (q.rear + 1) % q.capacity
	q.arr[q.rear] = data
	q.size = q.size + 1
	return nil
}

func (q *queue) Dequeue() (string, error) {
	if q.IsEmpty() {
		return "", errors.New("Queue is empty!")
	}
	d := q.arr[q.front]
	q.front = (q.front + 1) % q.capacity
	q.size = q.size - 1
	return d, nil
}
