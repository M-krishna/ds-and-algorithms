package main

import "fmt"

func LinearSearch(arr []int, target int) int {
	for _, v := range arr {
		if v == target {
			return v
		}
	}
	return -1
}

func main() {
	arr := []int{1,2,3,4,5}
	target := 51
	fmt.Println(LinearSearch(arr, target))
}