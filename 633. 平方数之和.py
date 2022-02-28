# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a^2 + b^2 = c.
#
# Example 1:
#
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
#
# Example 2:
#
# Input: 3
# Output: False

class Solution:
    def judgeSquareSum(self, c):
        i = 0
        hash_map = {}
        if c == 0:
            return True
        while (i-1) ** 2 <= c:
            if (c - (i-1)**2) in hash_map:
                return True
            else:
                hash_map[i**2] = True
                i += 1
                continue

        return False


if __name__ == '__main__':
    a = 4
    solution = Solution()
    c = solution.judgeSquareSum(a)
    print(c)