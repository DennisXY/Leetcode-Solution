# Given a binary tree, determine if it is height-balanced.

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def balance(self, pRoot):
        if not pRoot:
            return 0
        left = self.balance(pRoot.left)
        right = self.balance(pRoot.right)
        if left == -1 or right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

    def IsBalanced_Solution(self, pRoot):
        return self.balance(pRoot) != -1