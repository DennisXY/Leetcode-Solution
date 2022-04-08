# Given an n-ary tree, return the level order traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value.

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root):
        if not root:
            return list()
        stack, result = [root], list()
        while len(stack) > 0:
            temp = [i.val for i in stack]
            temp_stack = list()
            for i in stack:
                for j in i.children:
                    temp_stack.append(j)
            stack = temp_stack
            result.append(temp)
        return result

