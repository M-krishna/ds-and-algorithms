package main

import "fmt"

func heapify(arr []int, size, index int) {
	left := 2*index + 1
	right := 2*index + 2
	largest := index

	if left < size && arr[left] > arr[largest] {
		largest = left
	}
	if right < size && arr[right] > arr[largest] {
		largest = right
	}
	if largest != index {
		arr[index], arr[largest] = arr[largest], arr[index]
		heapify(arr, size, largest)
	}
}

func heapSort(arr []int) {
	n := len(arr)
	for i := (n / 2) - 1; i >= 0; i-- {
		heapify(arr, n, i)
	}

	// heap sort
	for i := n - 1; i >= 0; i-- {
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)
	}
}

func main() {
	arr := []int{10, 9, 8, 7, 6, 5}
	heapSort(arr)
	for _, v := range arr {
		fmt.Printf("%d ", v)
	}
}
