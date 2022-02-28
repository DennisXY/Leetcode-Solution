# Given two binary strings a and b, return their sum as a binary string.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)<len(b):
            a='0'*(len(b)-len(a))+a
        else:
            b='0'*(len(a)-len(b))+b
        carry=0
        res=''
        for i in range(len(a)-1,-1,-1):
            if int(a[i])+int(b[i])+carry>=2:
                res=str(int(a[i])+int(b[i])+carry-2)+res
                carry=1
            else:
                res=str(int(a[i])+int(b[i])+carry)+res
                carry=0
        if carry==1:
            res='1'+res
        return res