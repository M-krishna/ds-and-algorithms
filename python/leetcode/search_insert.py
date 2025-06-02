
from typing import List

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
----------
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
----------
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
----------
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
------------
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        return left
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert([1,3,5,6], 5))
    print(solution.searchInsert([1,3,5,6], 2))
    print(solution.searchInsert([1,3,5,6], 7))
    print(solution.searchInsert([1,3,5,6], 4))
    print(solution.searchInsert([1,4,5,6], 3))