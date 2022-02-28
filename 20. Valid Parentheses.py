# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
# Example 4:
#
# Input: s = "([)]"
# Output: false
# Example 5:
#
# Input: s = "{[]}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        brac = {'{': '}', '[': ']', '(': ')'}
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False

                while stack:
                    if brac[stack[-1]] == i:
                        stack.pop()
                        break
                    else:
                        return False
        if stack:
            return False
        return True