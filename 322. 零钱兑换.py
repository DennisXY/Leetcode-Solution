# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        coins.sort()
        if len(coins) == 0 or amount == 0:
            return 0
        for coin in coins:
            if coin > amount:
                break
            dp[coin] = 1
        for i in range(coins[0], amount+1):
            for coin in coins:
                if coin > i:
                    break
                dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[-1] != float('inf'):
            return dp[-1]
        else:
            return -1


if __name__ == '__main__':
    a = [2]
    b = 3
    solution = Solution()
    c = solution.coinChange(a,b)
    print(c)