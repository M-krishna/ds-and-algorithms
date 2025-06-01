"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
----------
Input: s = "()"
Output: true

Example 2:
----------
Input: s = "()[]{}"
Output: true

Example 3:
----------
Input: s = "(]"
Output: false

Example 4:
----------
Input: s = "([])"
Output: true

Constraints:
------------
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_parenthesis = ["{", "(", "["]
        closed_parenthesis = ["}", ")", "]"]
        brackets_map = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        for i in s:
            if i in open_parenthesis:
                stack.append(i)
            elif i in closed_parenthesis:
                if not stack:
                    return False
                peek_element = stack[-1]
                if brackets_map[peek_element] == i:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("([])"))
    print(solution.isValid("]"))