# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of
# a different word or phrase, typically using all the original letters
# exactly once.
#
#  
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for string in strs:
            temp = list(string)
            temp.sort()
            temp = str(temp)
            if temp not in result:
                result[temp] = list()
                result[temp].append(string)
            else:
                result[temp].append(string)
        temp = list()
        for key, value in result.items():
            temp.append(value)
        return temp