# 求给定二叉树的最大深度，
# 最大深度是指树的根结点到最远叶子结点的最长路径上结点的数量。


class Solution:

    def maxDepth(self, root):
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r) + 1