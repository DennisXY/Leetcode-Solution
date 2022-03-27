# Given an array of integers nums and an integer k,
# return the total number of subarrays whose sum equals to k.
#
# Example 1:
#
# Input: nums = [1,1,1], k = 2
# Output: 2

# 每次遇到“连续子数组的和”相关问题，我们都可以考虑前缀和是否能行。
# 我们使用字典记录每个前缀和的出现次数。依次遍历元素时，我们只能看到前面的前缀和，
# 所以直接相加即可。

from collections import *


class Solution:
    def subarraySum(self, nums, k: int) -> int:

        presum_map = defaultdict(int)
        presum_map[0] = 1
        presum, ans = 0, 0

        for i in range(len(nums)):
            presum += nums[i]
            target = presum - k # k == presum - target, 当前和减掉前面的和
            if target in presum_map:
                ans += presum_map[target]
            presum_map[presum] += 1

        return ans
