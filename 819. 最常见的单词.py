# Given a string paragraph and a string array of the banned words banned,
# return the most frequent word that is not banned. It is guaranteed there
# is at least one word that is not banned, and that the answer is unique.
#
# The words in paragraph are case-insensitive and the answer should be returned
# in lowercase.
#
# Example 1:
#
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",
# banned = ["hit"]
# Output: "ball"

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        freq = Counter()
        word, n = "", len(paragraph)
        for i in range(n + 1):
            if i < n and paragraph[i].isalpha():
                word += paragraph[i].lower()
            elif word:
                if word not in ban:
                    freq[word] += 1
                word = ""
        maxFreq = max(freq.values())
        return next(word for word, f in freq.items() if f == maxFreq)
