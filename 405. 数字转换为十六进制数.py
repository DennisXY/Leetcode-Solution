# Given an integer, write an algorithm to convert it to hexadecimal.
# For negative integer, two’s complement method is used.
#
# Note:
#
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s.
# If the number is zero, it is represented by a single zero character '0';
# otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.
# Example 1:
#
# Input:
# 26
#
# Output:
# "1a"
# Example 2:
#
# Input:
# -1
#
# Output:
# "ffffffff"

class Solution:
    def toHex(self, num: int) -> str:
        result = list()
        hex_ = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

        if num < 0:
            num = 4294967295 + 1 + num

        if num == 0:
            return '0'

        while num > 0:
            temp = num % 16
            if temp < 10:
                result.append(str(temp))
            else:
                result.append(hex_[temp])
            num //= 16

        result.reverse()
        return ''.join(result)