# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# Constraints:
# 1 <= n <= 45

class Solution:
    def climbStairs(self, n):
        if n < 3:
            return n
        climb = [0 for i in range(n)]
        climb[0], climb[1] = 1, 2
        for j in range(2, n):
            climb[j] = climb[j-1] + climb[j-2]
        return climb[n-1]