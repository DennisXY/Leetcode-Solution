# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside
# the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and
# that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
# Example 1:
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Same question 227


class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = list(), "", 0
        for i in s:
            if '0' <= i <= '9':
                multi = 10*multi + int(i)
            elif i == '[':
                stack.append([multi, res])
                multi = 0
                res = ""
            elif i == ']':
                multi_temp, res_temp = stack.pop()
                res = res_temp + multi_temp*res
            else:
                res += i
        return res