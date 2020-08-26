package main

import "fmt"


func merge(arr []int, l, m, r int) {
	// find the length of left and right array
	n1 := m-l+1
	n2 := r-m

	// create temp arrays
	L := make([]int, n1)
	R := make([]int, n2)

	// Copy the elements over to temp array
	for i := 0; i < n1; i++ {
		L[i] = arr[l+i]
	}
	for j := 0; j < n2; j++ {
		R[j] = arr[m+1+j]
	}

	// Start merging the left and right array
	i, j := 0, 0
	k := l

	for i < n1 && j < n2 {
		if L[i] <= R[j] {
			arr[k] = L[i]
			i++
		} else {
			arr[k] = R[j]
			j++
		}
		k++
	}

	// copy remaining elements of L[]
	for i < n1 {
		arr[k] = L[i]
		i++
		k++
	}

	// copy remaining elements of R[]
	for j < n2 {
		arr[k] = R[j]
		j++
		k++
	}
}

func sort(arr []int, l, r int) {
	if l < r {
		mid := (l+r)/2

		sort(arr, l, mid)
		sort(arr, mid+1, r)

		merge(arr, l, mid, r)
	}
	fmt.Println(arr)
}


func main() {
	arr := []int{38,27,43,3,9,82,10}
	l := 0
	r := len(arr) - 1
	sort(arr, l, r)
}