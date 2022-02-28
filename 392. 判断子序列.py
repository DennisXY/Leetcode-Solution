# Given a string s and a string t, check if s is subsequence of t.
#
# A subsequence of a string is a new string which is formed from the original string by
# deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
# (ie, "ace" is a subsequence of "abcde" while "aec" is not).
#
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
# and you want to check one by one to see if T has its subsequence.
# In this scenario, how would you change your code?
#
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution:
    def isSubsequence(self, s, t):
        s_idx = 0
        t_idx = 0
        len_s = len(s)
        len_t = len(t)
        if len_s == 0:
            return True
        if len_t == 0:
            return False
        while t_idx < len_t:
            if s[s_idx] == t[t_idx]:
                s_idx += 1
                t_idx += 1
            else:
                t_idx += 1

            if s_idx == len_s:
                return True
        return False


if __name__ == '__main__':
    a = "axc"
    b = "ahbgdc"
    solution = Solution()
    c = solution.isSubsequence(a, b)
    print(c)