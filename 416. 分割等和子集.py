# Given a non-empty array containing only positive integers,
# find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
#
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
#
# Example 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# dp[i][j] 表示从数组的[0,i]下标范围内选取若干个正整数，
# 是否存在一种选取方案使得被选取的正整数的和等于j


class Solution:
    def canPartition(self, nums):
        target = sum(nums)
        length = len(nums)

        if target % 2 == 1:
            return False
        half = int(target/2)

        dp = [[False] * (half + 1) for i in range(length)]
        dp[0][0] = True
        for i in range(1, half + 1):
            if nums[0] == i:
                dp[0][i] = True
                break

        for i in range(1, length):
            for j in range(half+1):
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    a = [1, 5, 11, 5]
    solution = Solution()
    c = solution.canPartition(a)
    print(c)
