# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
# Input: "hello"
# Output: "holle"
# Example 2:
#
# Input: "leetcode"
# Output: "leotcede"
class Solution:
    def reverseVowels(self, sr):
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
        sr_list = list(sr)
        start = 0
        end = len(sr) - 1
        while start <= end:
            if sr_list[start] in vowel:
                if sr_list[end] in vowel:
                    if sr_list[start] == sr_list[end]:
                        start += 1
                        end -= 1
                    else:
                        temp = sr_list[start]
                        sr_list[start] = sr_list[end]
                        sr_list[end] = temp
                        start += 1
                        end -= 1
                else:
                    end -= 1
            else:
                start += 1
        s = ''.join(sr_list)
        return s