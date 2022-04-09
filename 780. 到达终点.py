# A move consists of taking a point (x, y) and transforming it to either
# (x, x+y) or (x+y, y).
#
# Given a starting point (sx, sy) and a target point (tx, ty),
# return True if and only if a sequence of moves exists to
# transform the point (sx, sy) to (tx, ty). Otherwise, return False.
#
# Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)


class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        #DP method: running out of time
        # if sx > tx or sy >ty:
        #     return False
        # dp = [[False] * (ty+1) for i in range(tx+1)]
        # dp[sx][sy] = True
        # for i in range(sx, tx+1):
        #     for j in range (sy, ty+1):
        #         if i == sx and j == sy:
        #             continue
        #         if i - j > 0:
        #             dp[i][j] = dp[i-j][j]
        #         else:
        #             dp[i][j] = dp[i][j-i]
        #
        # return dp[tx][ty]

        # 反复使用 {tx, ty} 中较大的值减去较小的值更新点，到达点 {sx, sy} 时返回 true。使用模运算加速求解父点的过程。
        while sx < tx != ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx and ty == sy:
            return True
        elif tx == sx:
            return ty > sy and (ty - sy) % tx == 0
        elif ty == sy:
            return tx > sx and (tx - sx) % ty == 0
        else:
            return False


if __name__ == '__main__':
    a, b, c, d = 10, 2, 2, 11
    solution = Solution()
    c = solution.reachingPoints(a, b, c, d)
    print(c)
