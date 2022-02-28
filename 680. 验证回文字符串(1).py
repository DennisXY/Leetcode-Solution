# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.

class Solution:
    def validPalindrome(self, s):
        start, end = 0, len(s) - 1
        flag = True
        while start <= end:
            if s[start] == s[end]:
                if start == end or start == end-1:
                    return True
                start += 1
                end -= 1
                continue
            else:
                if not flag: # already delete once
                    return False
                elif s[start + 1] == s[end]:
                    #print(s[start + 1], s[end])
                    flag = False
                    start += 1
                    continue
                elif s[start] == s[end - 1]:
                    #print(s[start], s[end - 1])
                    flag = False
                    end -= 1
                    continue
                return False


if __name__ == '__main__':
    a = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    solution = Solution()
    c = solution.validPalindrome(a)
    print(c)