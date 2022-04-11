# Given an integer n, return the count of all numbers with unique digits
# Input: n = 2
# Output: 91
# 0 ≤ x < 100, excluding
# 11, 22, 33, 44, 55, 66, 77, 88, 99
# 排列组合，看官方题解
# https://leetcode-cn.com/problems/count-numbers-with-unique-digits/solution/tong-ji-ge-wei-shu-zi-du-bu-tong-de-shu-iqbfn/


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        res, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            res += cur
        return res
