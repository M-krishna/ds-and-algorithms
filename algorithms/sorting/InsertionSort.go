package main

import "fmt"

func insertionSort(arr []int) []int {
	l := len(arr)
	for i := 1; i < l; i++ {
		key := arr[i]
		j := i - 1

		for j >= 0 && arr[j] > key {
			arr[j+1] = arr[j]
			j = j - 1
		}
		arr[j+1] = key
	}
	return arr
}

func main() {
	arr := []int{4, 3, 2, 10, 12, 15, 6}
	fmt.Println(insertionSort(arr))
}
