from typing import List

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
----------
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
----------
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:
------------
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""


class Solution:
    def compare(self, s1: str, s2: str):
        i = 0
        characters = ""

        while ((i < len(s1)) and (i < len(s2))) and ((s1[i] == s2[i])):
            characters += s1[i]
            i += 1
        return characters

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]

        prefix = self.compare(strs[0], strs[1])
        for i in range(2, len(strs)):
            prefix = self.compare(prefix, strs[i])
            if not prefix:
                return ""
        return prefix

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    solution = Solution().longestCommonPrefix(strs)
    print(solution)
    str1 = ["dog","racecar","car"]
    solution = Solution().longestCommonPrefix(str1)
    print(solution)
