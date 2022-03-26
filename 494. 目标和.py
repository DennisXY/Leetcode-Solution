# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
# Now you have 2 symbols + and -.
# For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers
# equal to target S.
#
# Example 1:
#
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.

# 转化为0-1背包问题，选取的元素加起来要等于正数和
# a+b = sum, b-a = target, -> b(正数和) = (sum+target)/2
# dp[i][j] 选取第i个元素，正数和为j
# 若nums[i]取正号，dp[i][j] = dp[i-1][j-nums[i]]；
# 若nums[i]取负号，dp[i][j] = dp[i-1][j]。（因为j为正数和，取负号并不会改变正数和）


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (target+sum(nums))%2!=0:
            return 0
        total = (target+sum(nums))//2 # 定义正数和为total
        if total < 0: # 正数和为负，返回0
            return 0
        dp = [[0 for _ in range(total+1)] for _ in range(len(nums))]
        for j in range(total+1): # 初始化第一行
            if nums[0] == j:
                dp[0][j] = 1
        dp[0][0] += 1 # 初始化第一行后，[0][0]自增1，到此才算初始化结束
        for i in range(1, len(nums)):
            for j in range(total+1):
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]