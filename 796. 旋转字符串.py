# Given two strings s and goal, return true if and only if s can
# become goal after some number of shifts on s.
#
# A shift on s consists of moving the leftmost character of s to the
# rightmost position.
#
# For example, if s = "abcde", then it will be "bcdea" after one shift.
#  
# Example 1:
#
# Input: s = "abcde", goal = "cdeab"
# Output: true

# 字符串 s + ss+s 包含了所有 ss 可以通过旋转操作得到的字符串，
# 只需要检查goal 是否为 s + ss+s 的子字符串即可


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
