# Given an integer array nums, you need to find one continuous subarray
# that if you only sort this subarray in ascending order,
# then the whole array will be sorted in ascending order.
#
# Return the shortest such subarray and output its length.
#
# Example 1:
#
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to
# make the whole array sorted in ascending order.

# 弱智方法：复制数组然后排序，跟原数组比对

# 厉害方法：三个数组numA + numB + numC = 原数组
# numB为需要排序的那部分，每个numA里面的元素都小于numB/C，每个numC里面元素都小于numA/B
# 从而可以确定numA和numC的边界


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1
        # numB的左右边界right &  left

        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]

            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]

        return 0 if right == -1 else right - left + 1
