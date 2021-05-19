// Go Implementation on min heap
package main

import (
	"fmt"
	"math"
)

type MinHeap struct {
	capacity int
	size int
	dataArr []int
}

func NewMinHeap(capacity int) *MinHeap {
	return &MinHeap{
		capacity: capacity,
		size: 0,
		dataArr: make([]int, 0),
	}
}

func (h *MinHeap) parent(index int) int {
	return (index - 1) / 2
}

func (h *MinHeap) leftChild(index int) int {
	return (2*index) + 1
}

func (h *MinHeap) rightChild(index int) int {
	return (2*index) + 2
}

func (h *MinHeap) swap(first, second int) {
	h.dataArr[first], h.dataArr[second] = h.dataArr[second], h.dataArr[first]
}

func (h *MinHeap) insert(data int) error{
	if h.size == h.capacity {
		return fmt.Errorf("Heap Overflow")
	}

	h.dataArr = append(h.dataArr, data)
	h.size++
	h.debounce(h.size - 1)
	return nil
}

// After inserting a new element into a heap we need to debounce to check if the heap is verified
func (h *MinHeap) debounce(index int) {
	for h.dataArr[index] < h.dataArr[h.parent(index)] {
		h.swap(index, h.parent(index))
		index = h.parent(index)
	}
}

func (h *MinHeap) peek() error {
	if h.size == 0 {
		return fmt.Errorf("Heap is empty!")
	}
	fmt.Println(h.dataArr[0])
	return nil
}

// Delete a specific key at the index
func (h *MinHeap) deleteKey(index int) {
	h.decreaseKey(index, math.Inf(-1))
	h.extractMin()
}

// Decrease the value of key in index with the new_value. 
// It is assumed that the new_value is less than h.dataArr[index]
func (h *MinHeap) decreaseKey(index int, new_value float64) {
	h.dataArr[index] = int(new_value)
	for index != 0 && h.dataArr[index] < h.dataArr[h.parent(index)] {
		h.swap(index, h.parent(index))
		index = h.parent(index)
	} 
}

// Method to remove minimum element (or the root) from min heap
func (h *MinHeap) extractMin() int {
	if h.size == 1 {
		h.size--
		data := h.dataArr[0]
		h.dataArr = []int{}
		return data
	}

	root := h.dataArr[0]
	h.dataArr[0] = h.dataArr[h.size - 1]
	h.dataArr = h.dataArr[:(h.size) - 1]
	h.size--
	h.minHeapify(0)
	return root
}

func (h *MinHeap) minHeapify(index int) {
	left := h.leftChild(index)
	right := h.rightChild(index)
	smallest := index

	if left < h.size && h.dataArr[left] < h.dataArr[smallest] {
		smallest = left
	}
	if right < h.size && h.dataArr[right] < h.dataArr[smallest] {
		smallest = right
	}

	if smallest != index {
		h.swap(index, smallest)
		h.minHeapify(smallest)
	}
}

func (h *MinHeap) buildMinHeap() {
	for index := ((h.size / 2) - 1); index >= 0; index-- {
		h.minHeapify(index)
	} 
}


func main() {
	// create a new min heap
	arr := []int{3,2,1,15,5,4,45}
	length := len(arr)
	heap := NewMinHeap(length)

	// insert elements one by one to the heap
	for i := 0; i < length; i++ {
		heap.insert(arr[i])
	}

	fmt.Println(heap.dataArr, heap.size)
	heap.peek()

	fmt.Println(heap.extractMin())
	heap.peek()

	fmt.Println(heap.dataArr, heap.size)

	fmt.Println(heap.extractMin())
	heap.peek()

	fmt.Println(heap.dataArr, heap.size)

	heap.decreaseKey(3, 1)
	fmt.Println(heap.dataArr, heap.size)

	heap.deleteKey(2)
	fmt.Println(heap.dataArr, heap.size)

	heap.buildMinHeap()
	fmt.Println(heap.dataArr, heap.size)
}