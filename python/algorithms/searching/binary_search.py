# Binary search can only be done in a sorted array
# Eg. [1,2,5,7,9,10] -> sorted in ascending order

from __future__ import annotations


def search_iteratively(arr: list, item: int, left: int, right: int) -> int:

    while left <= right:
        mid = (left + right) // 2

        if item == arr[mid]:
            return mid
        elif item < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1  # if the element is not found


def search_recursively(arr: list, item: int, left: int, right: int) -> int:
    if left > right:
        return -1  # return -1 if the item is not found in the list

    mid = (left + right) // 2

    if item == arr[mid]:
        return mid
    elif item < arr[mid]:
        return search_recursively(arr, item, left, mid - 1)
    else:
        return search_recursively(arr, item, mid + 1, right)


if __name__ == "__main__":
    arr = [1, 2, 4, 5, 7, 9, 10]
    item = 5
    left = 0
    right = len(arr) - 1
    result = search_iteratively(arr, item, left, right)
    print(result)

    result = search_recursively(arr, item, left, right)
    print(result)
