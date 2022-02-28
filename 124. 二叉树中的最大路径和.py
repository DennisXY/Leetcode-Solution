# A path in a binary tree is a sequence of nodes where
# each pair of adjacent nodes in the sequence has an edge connecting them.
# A node can only appear in the sequence at most once.
# Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of
# any non-empty path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.result = -float('inf')

    def maxPathSum(self, root) -> int:
        def max_check(root):
            if not root:
                return 0
            left = max(max_check(root.left), 0)
            right = max(max_check(root.right), 0)
            self.result = max(self.result, left + right + root.val)
            return root.val + max(left, right)

        max_check(root)
        return self.result