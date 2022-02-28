# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
# Example 1:
#
# Input: 1
# Output: "A"
# Example 2:
#
# Input: 28
# Output: "AB"
# Example 3:
#
# Input: 701
# Output: "ZY"

class Solution:
    def convertToTitle(self, n: int) -> str:
        result = list()
        a = [chr(i) for i in range(65, 91)]
        while n > 0:
            n -= 1
            temp = n%26
            result.append(chr(temp+65))
            n //= 26
        result.reverse()
        #print(result)
        temp = ''.join(result)
        return temp