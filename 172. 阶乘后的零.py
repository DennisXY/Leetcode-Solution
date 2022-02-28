# Given an integer n, return the number of trailing zeroes in n!
# Example 1:
#
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:
#
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Example 3:
#
# Input: n = 0
# Output: 0

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        if n < 5:
            return 0
        for i in range(5, n+1, 5):
            while i % 5 == 0:
                result += 1
                i //= 5
        return result