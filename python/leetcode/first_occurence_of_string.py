"""
Given two strings needle and haystack, return the index of the first occurrence 
of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
----------
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.


Example 2:
----------
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:
------------
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # base cases
        if len(haystack) == 0: return -1
        if len(needle) == 0: return 0
        if len(needle) > len(haystack): return -1

        needle_pointer = 0
        haystack_pointer = 0
        start_index = haystack_pointer

        while haystack_pointer < len(haystack) and needle_pointer < len(needle):

            if needle[needle_pointer] == haystack[haystack_pointer]:
                needle_pointer += 1
                if needle_pointer == len(needle):
                    return start_index
                haystack_pointer += 1
            else:
                start_index += 1
                needle_pointer = 0
                haystack_pointer = start_index
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.strStr("leetcode", "leetco"))
    print(solution.strStr("sadbutsad", "sad"))
    print(solution.strStr("butsadbut", "sad"))
    print(solution.strStr("hello", ""))
    print(solution.strStr("", "a"))
    print(solution.strStr("abc", "abcd"))
    print(solution.strStr("mississippi", "issip")) # edge case
    print(solution.strStr("aaa", "aa"))