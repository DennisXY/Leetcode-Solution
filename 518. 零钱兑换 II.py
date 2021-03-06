# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that amount.
# You may assume that you have infinite number of each kind of coin.
#
# Example 1:
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:
#
# Input: amount = 10, coins = [10]
# Output: 1

class Solution:
    def change(self, amount, coins):
        dp = [0 for i in range(amount + 1)]
        length = len(coins)
        if length == 0:
            return 0
        if amount == 0:
            return 1

        coins.sort()
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                if coin > i:
                    break
                dp[i] += dp[i-coin]
        if dp[-1] != 0:
            return dp[-1]
        else:
            return 0


if __name__ == '__main__':
    # a = 5
    # b = [1, 2, 5]
    # solution = Solution()
    # c = solution.change(a,b)
    # print(c)

    yes_votes = 42_572_654
    no_votes = 43_132_495
    precentage = (yes_votes+no_votes)/yes_votes
    print('{:-9} YES votes {:3.3%}'.format(yes_votes, precentage))