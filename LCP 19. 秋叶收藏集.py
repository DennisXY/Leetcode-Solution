# 小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves，
# 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
# 出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，
# 但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。
#
# 示例 1：
# 输入：leaves = “rrryyyrryyyrr”
# 输出：2
# 解释：调整两次，将中间的两片红叶替换成黄叶，得到 “rrryyyyyyyyrr”
#
# 示例 2：
# 输入：leaves = “ryr”
# 输出：0
# 解释：已符合要求，不需要额外操作
#
# 提示：
# 3 <= leaves.length <= 10^5
# leaves 中只包含字符 ‘r’ 和字符 ‘y’

#用3个状态分别表示其中的每一部分，即状态0和状态2分别表示前面和后面的红色部分，状态1表示黄色部分。

class Solution:
    def minimumOperations(self, leaves: str) -> int:

        def isRed(a):
            if a == 'r':
                return 0
            else:
                return 1

        def isYellow(a):
            if a == 'y':
                return 0
            else:
                return 1

        dp = [[0, 0, 0] for i in range(len(leaves))]
        #dp[i][0]: 第一次全红长度
        #dp[i][1]: 加上黄叶长度
        #dp[i][2]: 加上第二次红叶长度
        dp[0][1] = dp[0][2] = dp[1][2] = float("inf")
        if leaves[0] == 'r':
            dp[0][0] = 0
        else:
            dp[0][0] = 1

        for i in range(1, len(leaves)):
            dp[i][0] = dp[i - 1][0] + isRed(leaves[i])
            dp[i][1] = min(dp[i - 1][1], dp[i - 1][0]) + isYellow(leaves[i])
            dp[i][2] = min(dp[i - 1][2], dp[i - 1][1]) + isRed(leaves[i])
        return dp[len(leaves) - 1][2]

#用三个变量代替状态数组，即可将空间复杂度降低到 O(1).
class Solution2:
    def minimumOperations(self, leaves: str) -> int:

        def isRed(a):
            if a == 'r':
                return 0
            else:
                return 1

        def isYellow(a):
            if a == 'y':
                return 0
            else:
                return 1

        mid = float('inf')
        end = float('inf')

        if leaves[0] == 'r':
            front = 0
        else:
            front = 1

        for i in range(1, len(leaves)):

            if i == 1:
                end = float('inf')
            else:
                end = min(end, mid) + isRed(leaves[i])
            mid = min(mid, front) + isYellow(leaves[i])
            front = front + isRed(leaves[i])
        return end