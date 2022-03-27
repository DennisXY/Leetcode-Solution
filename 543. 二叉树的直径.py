# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the
# number of edges between them.
# 不能直接用最大深度之和，因为这条线路有可能不经过root，需要维持一个self.result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.result = 1
        def max_depth(root):
            if not root:
                return 0
            l = max_depth(root.left)
            r = max_depth(root.right)
            self.result = max(self.result,l+r+1)
            return max(l, r) + 1
        max_depth(root)
        return self.result-1


