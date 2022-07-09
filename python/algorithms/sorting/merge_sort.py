# Time complexity: O(n log n)
# Auxilary space: O(n) # because of recursion
from __future__ import annotations


def mergeSort(arr):
    if len(arr) > 1:

        # find mid
        mid = len(arr) // 2

        L = arr[:mid]  # left array

        R = arr[mid:]  # right array

        mergeSort(L)
        mergeSort(R)

        # once we splitted the array down to a single item. we can start comparing left and right array element and put it in a new array
        # declare 3 variables i,j,k
        # i is used to track L array items
        # j is used to track R array items
        # k is used to insert the sorted item in a new array
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # The below 2 loops are used to sort if there are any remaining items
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    mergeSort(arr)
    print(arr)
