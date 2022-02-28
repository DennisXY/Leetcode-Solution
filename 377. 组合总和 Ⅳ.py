# Given an integer array with all positive numbers and no duplicates,
# find the number of possible combinations that add up to a positive integer target.
#
# Example:
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
#
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?

class Solution:
    def combinationSum4(self, nums, target):
        length = len(nums)
        if length == 0 or target == 0:
            return 0
        dp = [0 for i in range(target+1)]
        dp[0] = 1

        for i in range(target + 1):
            for num in nums:
                if i < num:
                    continue
                dp[i] += dp[i-num]
        return dp[-1]


if __name__ == '__main__':
    a = [9]
    b = 3
    solution = Solution()
    x = solution.combinationSum4(a, b)
    print(x)