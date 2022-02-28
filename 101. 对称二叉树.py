# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)
        return check(root, root)