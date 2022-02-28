# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all keys
# greater than the original key in BST.
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs (root: TreeNode):
            nonlocal root, total
            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)
            return

        total = 0
        dfs(root)
        return root