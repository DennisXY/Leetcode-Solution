# Given an array of integers nums containing n + 1 integers
# where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums 
# and uses only constant extra space.
#
# Example 1:
#
# Input: nums = [1,3,4,2,2]
# Output: 2

#官方题解 二分法
# https://leetcode-cn.com/problems/find-the-duplicate-number/solution/xun-zhao-zhong-fu-shu-by-leetcode-solution/


class Solution:
    def findDuplicate(self, nums) -> int:
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt > mid:
                right = mid
            else:
                left = mid + 1
        return left
