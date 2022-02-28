# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:
#
# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# 需要返回最小字符串版本
class Solution:
    def LIS(self, arr):
        length = len(arr)
        dp = [1] * length
        for i in range(length - 2, -1, -1):
            for j in range(length - 1, i, -1):
                if arr[i] < arr[j] and dp[i] <= dp[j]:
                    dp[i] += 1
        max_length = max(dp)
        temp = max_length
        result = list()

        for i in range(length):
            if dp[i] == max_length:
                min_idx = i
                for j in range(i, length):
                    if dp[j] != dp[i]:
                        i = j - 1
                        break
                    if arr[min_idx] > arr[j]:
                        if not result or arr[j] > result[-1]:
                            min_idx = j
                result.append(arr[min_idx])
                max_length -= 1
        return result