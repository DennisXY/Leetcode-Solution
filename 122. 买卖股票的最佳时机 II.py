# Say you have an array prices for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like
#
# Note: You may not engage in multiple transactions at the same time.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#       Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

class Solution:
    def maxProfit(self, prices):
        profit = 0
        length = len(prices) - 1
        for i in range(length):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
        return profit

if __name__ == '__main__':
    a = [7,1,5,3,6,4]
    solution = Solution()
    c = solution.maxProfit(a)
    print(c)