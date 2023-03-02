'''
I/P: [1,2,3,4,5]
O/P: [1, 3, 6, 10, 15]
'''

def prefix_sum(arr):
    result_arr = [0] * len(arr)

    prefix = 0
    for i in range(len(arr)):
        prefix += arr[i]
        result_arr[i] = prefix
    print(result_arr)

if __name__ == "__main__":
    prefix_sum([1,2,3,4,5])