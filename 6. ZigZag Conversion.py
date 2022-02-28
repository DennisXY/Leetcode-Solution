# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        result = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            result[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(result)