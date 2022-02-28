# Given a string s, remove duplicate letters so that every letter appears once and only once.
# You must make sure your result is the smallest in lexicographical order among all possible results.
#
# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
#
# Example 1:
#
# Input: s = "bcabc"
# Output: "abc"
# Example 2:
#
# Input: s = "cbacdcbc"
# Output: "acdb"

# 求解以下条件：
# 1.字符出现一次，顺序不变
# 2.字符多次出现取排序小的
#
# 循环条件 stack and char < stack[-1] and stack[-1] in s[idx:]


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = list()
        for idx, char in enumerate(s):
            if char in stack:
                continue
            else:
                while stack and stack[-1] > char and stack[-1] in s[idx:]:
                    stack.pop()
                stack.append(char)
        return "".join(stack)