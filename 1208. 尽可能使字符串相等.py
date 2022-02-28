# You are given two strings s and t of the same length. You want to change s to t.
# Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is,
# the absolute difference between the ASCII values of the characters.
#
# You are also given an integer maxCost.
#
# Return the maximum length of a substring of s that can be changed to be the same as
# the corresponding substring of twith a cost less than or equal to maxCost.
#
# If there is no substring from s that can be changed to its corresponding substring from t, return 0.
#
# Example 1:
#
# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.
# Example 2:
#
# Input: s = "abcd", t = "cdef", maxCost = 3
# Output: 1
# Explanation: Each character in s costs 2 to change to charactor in t, so the maximum length is 1.
# Example 3:
#
# Input: s = "abcd", t = "acde", maxCost = 0
# Output: 1
# Explanation: You can't make any change, so the maximum length is 1.

#滑动窗口
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        length = len(s)
        gap = [abs(ord(s[i]) - ord(t[i])) for i in range(length)]
        start, end, maxLength = 0, 0, 0
        total = 0
        #窗口右侧右移
        while end < length:
            total += gap[end]
            while total > maxCost:
                #窗口左侧右移
                total -= gap[start]
                start += 1
            maxLength = max(maxLength, end - start + 1)
            end += 1
        return maxLength