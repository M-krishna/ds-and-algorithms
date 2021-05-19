package main

import "fmt"

func selectionSort(arr []int) []int {
	l := len(arr)
	for i := 0; i < l-1; i++ {
		small := i
		for j := i+1; j < l; j++ {
			if arr[j] < arr[small] {
				small = j
			}
		}
		arr[small], arr[i] = arr[i], arr[small]
	}
	return arr
}

func main() {
	arr := []int{14,33,27,10,35,19,42,44}
	fmt.Println(selectionSort(arr))
}