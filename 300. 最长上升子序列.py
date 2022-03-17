# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101],
# therefore the length is 4.
# Note:
#
# There may be more than one LIS combination, it is only necessary
# for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# nlog版本 贪心+二分
# 官方题解 part 2：
# https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
class Solution:
    def lengthOfLIS(self, nums) -> int:
        d = []
        #  d[i]，表示长度为i的最长上升子序列的末尾元素的最小值
        # 用 len 记录目前最长上升子序列的长度，起始时len为1，d[1]=nums[0]

        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)


# 需要返回最小字符串版本
class Solution:
    def LIS(self, nums):
        length = len(nums)
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(dp)
        result = list()

        for i in range(length):
            if dp[i] == max_length:
                min_idx = i
                for j in range(i, length):
                    if dp[j] != dp[i]:
                        i = j - 1
                        break
                    if nums[min_idx] > nums[j]:
                        if not result or nums[j] > result[-1]:
                            min_idx = j
                result.append(nums[min_idx])
                max_length -= 1
        return result