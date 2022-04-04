# Given two integers left and right, return the count of numbers in the
# inclusive range [left, right] having a prime number of set bits in
# their binary representation.
#
# Recall that the number of set bits an integer has is the number of 1's
# present when written in binary.
#
# For example, 21 written in binary is 10101, which has 3 set bits.
# Input: left = 6, right = 10
# Output: 4
# Explanation:
# 6  -> 110 (2 set bits, 2 is prime)
# 7  -> 111 (3 set bits, 3 is prime)
# 8  -> 1000 (1 set bit, 1 is not prime)
# 9  -> 1001 (2 set bits, 2 is prime)
# 10 -> 1010 (2 set bits, 2 is prime)
# 4 numbers have a prime number of set bits.

# 二进制中 11 的个数不会超过19，而不超过19的质数只有2, 3, 5, 7, 11, 13, 17, 19
# 可以用一个二进制数mask=665772=10100010100010101100来存储这些质数


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(((1 << x.bit_count()) & 665772) != 0 for x in range(left, right + 1))

