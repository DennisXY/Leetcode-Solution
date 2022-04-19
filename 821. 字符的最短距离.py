# Given a string s and a character c that occurs in s, return an array of
# integers answer where answer.length == s.length and answer[i] is the
# distance from index i to the closest occurrence of character c in s.
#
# The distance between two indices i and j is abs(i - j), where abs is
# the absolute value function.
#
# Example 1:
#
# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]


class Solution:
    def shortestToChar(self, s: str, c: str):
        match_idx, result = list(), list()
        length = len(s)
        for i in range(length):
            if s[i] == c:
                match_idx.append(i)
        for i in range(length):
            if s[i] == c:
                result.append(0)
            else:
                if match_idx[0] > i:
                    result.append(match_idx[0]-i)
                elif match_idx[-1] < i:
                    result.append(i-match_idx[-1])
                else:
                    for j in range(len(match_idx)):
                        if match_idx[j] > i:
                            result.append(min(match_idx[j]-i, i-match_idx[j-1]))
                            break
        return result