// Implementation of Queue using 1D Array

package main

import "fmt"

type Queue struct {
	Front    int
	Rear     int
	Array    []int
	Capacity int
	Size     int
}

func NewQueue(capacity int) *Queue {
	return &Queue{
		Front:    0,
		Rear:     capacity - 1,
		Array:    make([]int, capacity),
		Capacity: capacity,
		Size:     0,
	}
}

func (q *Queue) IsFull() bool {
	return q.Size == q.Capacity
}

func (q *Queue) IsEmpty() bool {
	return q.Size == 0
}

func (q *Queue) Peek() {
	if q.IsEmpty() {
		fmt.Println("Queue is empty!")
		return
	}
	fmt.Println(q.Array[q.Rear])
}

func (q *Queue) EnQueue(data int) {
	if q.IsFull() {
		fmt.Println("Queue Overflow")
		return
	}
	q.Rear = (q.Rear + 1) % q.Capacity
	q.Array[q.Rear] = data
	q.Size = q.Size + 1
}

func (q *Queue) DeQueue() {
	if q.IsEmpty() {
		fmt.Println("Queue is empty")
		return
	}
	item := q.Array[q.Front]
	q.Front = (q.Front + 1) % q.Capacity
	q.Size = q.Size - 1
	fmt.Println(item)
}

func main() {
	q := NewQueue(5)
	fmt.Println(q.IsFull())
	fmt.Println(q.IsEmpty())
	q.Peek()
	q.EnQueue(1)
	q.EnQueue(2)
	q.EnQueue(3)
	q.EnQueue(4)
	q.EnQueue(5)
	q.DeQueue()
	q.DeQueue()
	q.DeQueue()
	q.DeQueue()
	q.DeQueue()
	fmt.Println(q.Size)
	q.Peek()
}
