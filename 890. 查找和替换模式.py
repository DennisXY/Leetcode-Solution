# iven a list of strings words and a string pattern, return a list of words[i]
# that match pattern. You may return the answer in any order.
#
# A word matches the pattern if there exists a permutation of letters p so that
# after replacing every letter x in the pattern with p(x), we get the desired word.
#
# Recall that a permutation of letters is a bijection from letters to letters:
# every letter maps to another letter, and no two letters map to the same letter.
#
# Example 1:
#
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def conv(word):
            result = list()
            temp = dict()
            for c in word:
                if c not in temp:
                    temp[c] = len(temp) + 1
                    result.append(temp[c])
                else:
                    result.append(temp[c])
            return result

        patt = conv(pattern)
        final = list()
        for word in words:
            temp = conv(word)
            if temp == patt:
                final.append(word)
        return final
