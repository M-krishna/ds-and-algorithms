'''
Product of an array except self
I/P: [1,2,3,4]
O/P: [24, 12, 8, 6]
'''

def product_except_self(arr):
    # Brute force approach
    # O(n^2)
    i = 0
    result_arr = [0] * len(arr)

    for i in range(len(arr)):
        curr_prod = 1
        for j in range(len(arr)):
            if i != j:
                curr_prod *= arr[j]
        result_arr[i] = curr_prod
    print(result_arr)


def product_except_self_optimal(arr):
    # Optimal solution using prefix and postfix approach
    # O(n)
    result_arr = [0] * len(arr)
    prefix = 1
    for i in range(len(arr)):
        result_arr[i] = prefix
        prefix *= arr[i]

    postfix = 1
    for i in range(len(arr) - 1, -1, -1):
        result_arr[i] *= postfix
        postfix *= arr[i]
    
    print(result_arr)

if __name__ == "__main__":
    product_except_self([1,2,3,4])
    product_except_self([4,3,2,1])
    product_except_self_optimal([1,2,3,4])