/*
Interpolation Search
*/

package main

import "fmt"

// Iterative method
func interpolationSearch(arr []int, target int) int {
	low := 0
	high := len(arr) - 1

	for low <= high && target >= arr[low] && target <= arr[high] {
		mid := low + ((high - low) / (arr[high] - arr[low])) * (target - arr[low])

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

// Recursive Method
func interpolationSearchRecursive(arr []int, low, high, target int) int {
	if low <= high && target >= arr[low] && target <= arr[high] {
		mid := low + ((high - low) / (arr[high] - arr[low])) * (target - arr[low])

		if arr[mid] == target {
			return mid
		} else if arr[mid] < target {
			return interpolationSearchRecursive(arr, mid+1, high, target)
		} else {
			return interpolationSearchRecursive(arr, low, mid-1, target)
		}
	}
	return -1
}

func main() {
	arr := []int{1,2,3,4,5,6,7,8,9,10}
	target := 11
	// fmt.Println(interpolationSearch(arr, target))

	low := 0
	high := len(arr) - 1
	fmt.Println(interpolationSearchRecursive(arr, low, high, target))
}