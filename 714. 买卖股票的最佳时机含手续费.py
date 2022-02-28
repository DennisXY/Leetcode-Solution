# Your are given an array of integers prices,
# for which the i-th element is the price of a given stock on day i;
# and a non-negative integer fee representing a transaction fee.
#
# You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
# You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
#
# Return the maximum profit you can make.
#
# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# Note:
#
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.

class Solution:
    def maxProfit(self, prices, fee):
        length = len(prices)
        dp = [[0] * 4 for i in range(length+1)]
        # dp[i][0]: 手上持有股票的最大收益
        # dp[i][1]: 手上不持有股票，在i卖出
        # dp[i][2]: 手上不持有股票，之前卖出
        f = [[-prices[0], 0, 0]] + [[0] * 3 for i in range(length - 1)]
        for i in range(1, length):
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i], f[i-1][1] - prices[i])
            f[i][1] = f[i - 1][0] + prices[i] - fee
            f[i][2] = max(f[i - 1][1], f[i - 1][2])

        return max(f[length - 1][1], f[length - 1][2])

if __name__ == '__main__':
    a = [1,3,7,5,10,3]
    b = 3
    solution = Solution()
    c = solution.maxProfit(a, b)
    print(c)