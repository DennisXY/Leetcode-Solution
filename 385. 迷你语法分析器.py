# Given a string s represents the serialization of a nested list,
# implement a parser to deserialize it and return the deserialized NestedInteger.
#
# Each element is either an integer or a list whose elements may also be integers or other lists.
#
# Example 1:
#
# Input: s = "324"
# Output: 324
# Explanation: You should return a NestedInteger object which contains a
# single integer 324.

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        stack, num, negative = [], 0, False
        for i, c in enumerate(s):
            if c == '-':
                negative = True
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append(NestedInteger())
            elif c in ',]':
                if s[i-1].isdigit():
                    if negative:
                        num = -num
                    stack[-1].add(NestedInteger(num))
                num, negative = 0, False
                if c == ']' and len(stack) > 1:
                    stack[-2].add(stack.pop())
        print(stack)
        return stack.pop()

