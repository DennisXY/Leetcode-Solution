# Suppose you have a long flowerbed in which some of the plots are planted and some are not.
# However, flowers cannot be planted in adjacent plots
# - they would compete for water and both would die.
#
# Given a flowerbed (represented as an array containing 0 and 1,
# where 0 means empty and 1 means not empty), and a number n,
# return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
#
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# Note:
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        length = len(flowerbed)
        if length == 0:
            return False
        cur_idx = 0
        while cur_idx < length:
            if cur_idx == length - 1: # last element
                if flowerbed[cur_idx] == 0 and flowerbed[cur_idx-1] == 0:
                    n -= 1
                break

            if flowerbed[cur_idx] == 1:
                cur_idx += 2
                continue

            else:
                if flowerbed[cur_idx + 1] == 0:
                    n -= 1
                    cur_idx += 2
                else:
                    cur_idx += 1

        if n <= 0:
            return True
        else:
            return False


if __name__ == '__main__':
    a = [1,0,0,0,1,0,0]
    solution = Solution()
    c = solution.canPlaceFlowers(a, 2)
    print(c)
