package main

import "fmt"

// This function will run in O(n2)
func bubbleSort(arr []int) []int{
	l := len(arr)
	for i := 0; i < l-1; i++ {
		for j := 0; j < l-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
	return arr
}

// More optimized solution
// If the array is already sorted then we can break out the loop
func bubbleSortOptimzed(arr []int) []int {
	l := len(arr)
	for i := 0; i < l-1; i++ {
		swapped := false
		for j := 0; j < l-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = true
			}
		}
		if !swapped {
			break
		}
	}
	return arr
}



func main() {
	arr := []int{10,98,50,2,3,16}
	fmt.Println(bubbleSort(arr))
	sorted_array := []int{1,2,3,4,5,6}
	fmt.Println(bubbleSortOptimzed(sorted_array))
}