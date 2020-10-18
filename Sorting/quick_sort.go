package main 

import "fmt"

func qs(arr []int, l, r int) {
	if l >= r {
		return
	}
	p := partition(arr, l, r)

	qs(arr, l, p-1)
	qs(arr, p+1, r)

	fmt.Println(arr)
}

func partition(arr []int, l, r int) int{
	pivot := arr[r]
	i := l-1
	for j := l; j < r; j++ {
		if arr[j] < pivot {
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
		}
	}
	arr[i+1], arr[r] = arr[r], arr[i+1]
	return i+1
}

func main() {
	arr := []int{-2,-3,-1,98,20,0,1,18}
	l := 0
	r := len(arr)-1
	qs(arr, l, r)
}