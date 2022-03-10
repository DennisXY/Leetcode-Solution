# Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        def revert(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            revert(root.left)
            revert(root.right)

        revert(root)
        return root