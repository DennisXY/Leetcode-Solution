# Given a string s which represents an expression, evaluate this expression and return its value. 
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: s = "3+2*2"
# Output: 7
# Example 2:
#
# Input: s = " 3/2 "
# Output: 1
# Example 3:
#
# Input: s = " 3+5 / 2 "
# Output: 5

class Solution:
    def calculate(self, s: str) -> int:
        stack, num = list(), 0
        pre_op = "+"
        for idx, ch in enumerate(s):
            if '0' <= ch <= '9':
                num = 10*num + int(ch)
            if ch in '+-*/' or idx == len(s)-1:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop()*num)
                elif pre_op == '/':
                    stack.append(int(stack.pop()/num))
                num, pre_op = 0, ch
        return sum(stack)
