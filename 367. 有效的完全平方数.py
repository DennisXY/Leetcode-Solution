# Given a positive integer num, write a function which returns True
# if num is a perfect square else False.
#
# Follow up: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: num = 16
# Output: true
# Example 2:
#
# Input: num = 14
# Output: false

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqr_num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        if num in sqr_num:
            return True
        a = num // 10

        def find(left, right, target):
            # print(left, right)
            mid = (left+right)//2
            if mid*mid == target:
                return True
            if mid == left:
                return False
            if mid*mid > target:
                return find(left, mid, target)
            else:
                return find(mid, right,target)
        return find(0, a, num)