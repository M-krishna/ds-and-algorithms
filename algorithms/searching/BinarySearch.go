package main

import "fmt"

// Iterative Approach
func binarySearch(arr []int, target int) int {
	low := 0
	high := len(arr) - 1
	for low <= high {
		mid := low + (high - low) / 2
		if arr[mid] == target {
			return mid
		} else if arr[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return -1
}

// Recursive Approach
func binarySearchRecursive(arr []int, low, high, target int) int {
	if low <= high {
		mid := low + (high - low) / 2
		if arr[mid] == target {
			return mid
		} else if arr[mid] < target {
			return binarySearchRecursive(arr, mid+1, high, target)
		} else {
			return binarySearchRecursive(arr, low, mid-1, target)
		}
	}
	return -1
}

func main() {
	arr :=  []int{1,2,3,4,5,6,7,8,9,10}
	target := 81
	// fmt.Println(binarySearch(arr, target))

	// For Recursive Approach
	low := 0
	high := len(arr) - 1
	fmt.Println(binarySearchRecursive(arr, low, high, target))
}