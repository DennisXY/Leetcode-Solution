# Given a non-empty array of integers nums,
# every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity
# and use only constant extra space.
#
# 异或XOR位运算


from functools import *


class Solution:
    def singleNumber(self, nums) -> int:
        return reduce(lambda x, y: x ^ y, nums)
