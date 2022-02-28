# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
# Now you have 2 symbols + and -.
# For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
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

class Solution:
    def findTargetSumWays(self, nums, S):
        # total = sum(nums)
        # if abs(total) < abs(S): return 0  # 目标和太大
        #
        # length = len(nums)
        # dp = [[0] * 2001 for i in range(length+1)]
        # #dp[i][j] 前i个数凑出j的可能性
        #
        # dp[1][nums[0]] = 1
        # dp[1][-nums[0]] += 1
        # #在很多语言中，是不允许数组的下标为负数的
        # #由于数组中所有数的和不超过 1000，那么 j 的最小值可以达到 -1000
        # for i in range(2, length+1):
        #     for j in range(-total, total+1):
        #         dp[i][j + 1000] = dp[i-1][j-nums[i-1] + 1000] + dp[i-1][j+nums[i-1] + 1000]
        # return dp[-1][-1]
        length = len(nums)
        dp = {(0, 0): 1}
        for i in range(1, length + 1):
            for j in range(-sum(nums), sum(nums) + 1):
                dp[(i, j)] = dp.get((i - 1, j - nums[i - 1]), 0) + dp.get((i - 1, j + nums[i - 1]), 0)
        return dp.get((length, S), 0)


if __name__ == '__main__':
    a = [1, 1, 1, 1, 1]
    b = 3
    solution = Solution()
    c = solution.findTargetSumWays(a, b)
    print(c)