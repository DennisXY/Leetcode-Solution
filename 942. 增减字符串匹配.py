# A permutation perm of n + 1 integers of all the integers in the range [0, n]
# can be represented as a string s of length n where:
#
# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. If there are
# multiple valid permutations perm, return any of them.
#
# Example 1:
#
# Input: s = "IDID"
# Output: [0,4,1,3,2]

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lo = 0
        hi = n = len(s)
        perm = [0] * (n + 1)
        for i, ch in enumerate(s):
            if ch == 'I':
                perm[i] = lo
                lo += 1
            else:
                perm[i] = hi
                hi -= 1
        perm[n] = lo  # 最后剩下一个数，此时 lo == hi
        return perm
