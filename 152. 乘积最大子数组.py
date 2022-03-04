# Given an integer array nums, find a contiguous non-empty subarray
# within the array that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.
#
# A subarray is a contiguous subsequence of the array.
#
# Example 1:
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.


class Solution:
    def maxProduct(self, nums):
        # 构建数组DP
        length = len(nums)
        mindp = [-float('inf')] * length
        maxdp = [float('inf')] * length
        mindp[0] = maxdp[0] = nums[0]
        for i in range(1, length):
            mindp[i] = min(mindp[i-1]*nums[i], maxdp[i-1]*nums[i], nums[i])
            maxdp[i] = max(maxdp[i-1]*nums[i], mindp[i-1]*nums[i], nums[i])
        return max(max(mindp), max(maxdp))

    def maxProduct2(self, nums):
        # 只需要两个变量DP
        length = len(nums)
        pre_min = pre_max = result = nums[0]
        for i in range(1, length):
            temp_min, temp_max = pre_min, pre_max
            pre_min = min(temp_min*nums[i], temp_max*nums[i], nums[i])
            pre_max = max(temp_max*nums[i], temp_min*nums[i], nums[i])
            result = max(result, pre_min, pre_max)
        return result
