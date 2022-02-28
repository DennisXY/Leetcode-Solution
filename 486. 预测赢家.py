# Given an array of scores that are non-negative integers.
# Player 1 picks one of the numbers from either end of the array followed by the player 2
# and then player 1 and so on. Each time a player picks a number,
# that number will not be available for the next player.
# This continues until all the scores have been chosen. The player with the maximum score wins.
#
# Given an array of scores, predict whether player 1 is the winner.
# You can assume each player plays to maximize his score.
#
# Example 1:
#
# Input: [1, 5, 2]
# Output: False
# Explanation:
# Initially, player 1 can choose between 1 and 2.
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5.
# If player 2 chooses 5, then player 1 will be left with 1 (or 2).
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
# Hence, player 1 will never be the winner and you need to return False.
#
# Example 2:
#
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7.
# No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

class Solution:
    def PredictTheWinner(self, nums):
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(nums[j] - dp[i][j - 1], nums[i] - dp[i + 1][j])
        return dp[0][-1] >= 0

        # 顺序不好颠倒。因为在这个递推公式里面：dp[i][j]=max(nums[j]-dp[i][j-1],nums[i]-dp[i+1][j]) .
        # dp[i][j] 是通过dp[i][j-1] 和dp[i+1][j]得到的，也就是必须先知道 dp[i][j-1] 和dp[i+1][j]，所以顺序不能颠倒。


if __name__ == '__main__':
    a = [3606449,6,5,9,452429,7,9580316,9857582,8514433,9,6,6614512,753594,5474165,4,2697293,8,7,1]
    solution = Solution()
    c = solution.PredictTheWinner(a)
    print(c)