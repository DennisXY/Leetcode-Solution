# Given two strings s and p, return an array of all the start indices of
# p's anagrams in s. You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.
#
# Example 1:
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# 自创骚方法：判断字符之和和平方和是不是相同的，如果都相同代表这个相同


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return list()
        sum_list, sum_list_add, result = 0, 0, list()
        length, start, end = len(p), 0, len(s)
        for i in p:
            sum_list += ord(i)
            sum_list_add += ord(i) ** 2
        temp, temp_add = 0, 0
        for i in range(length):
            temp += ord(s[i])
            temp_add += ord(s[i]) ** 2

        while start + length < end:
            if temp == sum_list and temp_add == sum_list_add:
                result.append(start)
            temp += (ord(s[start + length]) - ord(s[start]))
            temp_add += (ord(s[start + length]) ** 2 - ord(s[start]) ** 2)
            start += 1
        if temp == sum_list and temp_add == sum_list_add:
            result.append(start)

        return result