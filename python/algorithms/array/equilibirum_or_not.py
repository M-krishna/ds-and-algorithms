'''
Given an array of n integers, find if any index exists such that the sum of the elements to its
right is equal to the sum of elements to its left. If yes print the index, otherwise print "No Equilibrium"

I/P: [7,2,1,5,4]
O/P: 2
Explanation: Sum of elements to the left of index 2 is 7+2 = 9 and to the right of index 2 is 5+4=9

I/P: [23, 32, 12, 4]
O/P: No Equilibrium
Explanation: No such index exists for which the sum to its right and left is equal
'''

def equilibrium(arr):
    # Brute force solution
    # O(n^2)
    i = 1
    found = False
    while i < len(arr):
        left_sum = 0
        for j in range(0, i):
            left_sum += arr[j]
        
        right_sum = 0
        for k in range(i+1, len(arr)):
            right_sum += arr[k]
        
        if left_sum == right_sum:
            print(i)
            found = True
            break
        i += 1
    
    if not found:
        print("No Equilibrium")

def equilibrium_optimal(arr):
    # Using the prefix sum approach
    # O(n)
    left_sum = 0
    total_sum = sum(arr)
    found = False

    for i in range(len(arr)):
        total_sum = total_sum - arr[i]
        if left_sum == total_sum:
            print(i)
            found = True
            break
        left_sum += arr[i]
    
    if not found:
        print("No Equilibrium")

        
if __name__ == "__main__":
    equilibrium([7,2,1,5,4])
    equilibrium([23, 32, 12, 4])
    equilibrium_optimal([7,2,1,5,4])
    equilibrium_optimal([23, 32, 12, 4])