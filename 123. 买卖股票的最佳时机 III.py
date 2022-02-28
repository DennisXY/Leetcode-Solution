# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note:You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
#
#
# Example 1:
#
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:
#
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging
# multiple transactions at the same time. You must sell before buying again.
# Example 3:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# Example 4:
#
# Input: prices = [1]
# Output: 0


class Solution:
    def maxProfit(self, prices):
        #dp[i][j] in ith price, by manipulating j action, the most you can get.
        #j:
        #0: 第一次持有股票的最大收益
        #1：第一次没有股票
        #2：第二次持有股票的最大收益
        #3：第二次没有股票

        length = len(prices)
        if length == 1:
            return 0
        dp = [[-100000] * 4 for i in range(length)]
        dp[0][0] = -prices[0]

        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] - prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] + prices[i])
        return max(dp[-1][1], dp[-1][3], 0)

if __name__ == '__main__':
    a = [1]
    solution = Solution()
    c = solution.maxProfit(a)
    print(c)

