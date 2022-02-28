# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#
# Example 1:
#
# Input: x = 123
# Output: 321

class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x > 0 else -1
        x = abs(x)

        while x % 10 == 0 and x != 0:
            x //= 10
        result = 0
        while x // 10 != 0:
            result = result * 10 + (x % 10)
            x //= 10
        result = result * 10 + (x % 10)
        result *= flag

        return result if -2147483648 < result < 2147483647 else 0