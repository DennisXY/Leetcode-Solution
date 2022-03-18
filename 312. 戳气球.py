# You are given n balloons, indexed from 0 to n - 1.
# Each balloon is painted with a number on it represented by an array nums.
# You are asked to burst all the balloons.
#
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1]
# coins. If i - 1 or i + 1 goes out of bounds of the array,
# then treat it as if there is a balloon with a 1 painted on it.
#
# Return the maximum coins you can collect by bursting the balloons wisely.
#
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

# 戳气球的操作，发现这会导致两个气球从不相邻变成相邻，使得后续操作难以处理。
# 于是我们倒过来看这些操作，将全过程看作是每次添加一个气球。
# dp[i][j]表示填满开区间(i,j)能得到的最多硬币数


class Solution:
    def maxCoins(self, nums) -> int:
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)

        return rec[0][n + 1]
