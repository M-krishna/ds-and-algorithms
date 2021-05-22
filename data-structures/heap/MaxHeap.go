package main

import (
	"fmt"
)

type MaxHeap struct {
	capacity int
	size     int
	dataArr  []int
}

func NewMaxHeap(capacity int) *MaxHeap {
	return &MaxHeap{
		capacity: capacity,
		size:     0,
		dataArr:  make([]int, 0),
	}
}

func (h *MaxHeap) leaf(index int) bool {
	if index >= (h.size)/2 && index <= h.size {
		return true
	}
	return false
}

func (h *MaxHeap) parent(index int) int {
	return (index - 1) / 2
}

func (h *MaxHeap) leftChild(index int) int {
	return (2 * index) + 1
}

func (h *MaxHeap) rightChild(index int) int {
	return (2 * index) + 2
}

func (h *MaxHeap) insert(data int) error {
	if h.size >= h.capacity {
		return fmt.Errorf("Heap Overflow!")
	}
	h.dataArr = append(h.dataArr, data)
	h.size++
	h.debounce(h.size - 1)
	return nil
}

func (h *MaxHeap) debounce(index int) {
	for h.dataArr[index] > h.dataArr[h.parent(index)] {
		h.swap(index, h.parent(index))
		index = h.parent(index)
	}
}

func (h *MaxHeap) swap(first, second int) {
	h.dataArr[first], h.dataArr[second] = h.dataArr[second], h.dataArr[first]
}

func (h *MaxHeap) peek() error {
	if h.size == 0 {
		fmt.Errorf("Heap is empty!")
	}
	fmt.Println("Peak element is", h.dataArr[0])
	return nil
}

func (h *MaxHeap) extractMax() int {
	if h.size == 1 {
		h.size--
		data := h.dataArr[0]
		h.dataArr = []int{}
		return data
	}

	root := h.dataArr[0]
	h.dataArr[0] = h.dataArr[h.size-1]
	h.dataArr = h.dataArr[:(h.size)-1]
	h.size--
	h.maxHeapify(0)
	return root
}

func (h *MaxHeap) deleteKey(index int) error {
	if h.size <= index {
		return fmt.Errorf("Heap overflow!")
	}

	if h.leaf(index) {
		h.dataArr = h.dataArr[:(h.size)-1]
		h.size--
		h.maxHeapify(index)
		return nil
	}
	h.dataArr[index] = h.dataArr[h.size-1]
	h.dataArr = h.dataArr[:(h.size)-1]
	h.size--
	h.maxHeapify(index)
	return nil
}

func (h *MaxHeap) maxHeapify(index int) {
	left := h.leftChild(index)
	right := h.rightChild(index)
	largest := index

	if left < h.size && h.dataArr[left] > h.dataArr[largest] {
		largest = left
	}

	if right < h.size && h.dataArr[right] > h.dataArr[largest] {
		largest = right
	}

	if largest != index {
		h.swap(index, largest)
		h.maxHeapify(largest)
	}
}

func main() {
	arr := []int{3, 2, 1, 15, 5, 4, 45}
	length := len(arr)
	heap := NewMaxHeap(length)

	// insert
	for i := 0; i < length; i++ {
		heap.insert(arr[i])
	}

	heap.peek()
	fmt.Println(heap.dataArr, heap.size)

	heap.extractMax()
	heap.peek()
	fmt.Println(heap.dataArr, heap.size)

	err := heap.deleteKey(1)
	if err != nil {
		fmt.Println(err)
	}
	heap.peek()
	fmt.Println(heap.dataArr, heap.size)

	err = heap.deleteKey(4)
	if err != nil {
		fmt.Println(err)
	}
	heap.peek()
	fmt.Println(heap.dataArr, heap.size)
}
