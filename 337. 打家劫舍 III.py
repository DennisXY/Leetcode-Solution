# The thief has found himself a new place for his thievery again.
# There is only one entrance to this area, called root.
#
# Besides the root, each house has one and only one parent house.
# After a tour, the smart thief realized that all houses in
# this place form a binary tree. It will automatically contact the police
# if two directly-linked houses were broken into on the same night.
#
# Given the root of the binary tree, return the maximum amount of money
# the thief can rob without alerting the police.


# 经典的DP。
# 难点在于，如果从上往下看这棵树，是无法在遍历到某一个节点时决定【偷或不偷】
# 这个节点的收益的。
# 因此，我们要想办法从下往上看，于是就想到了后序遍历。
# 想到后序遍历，接下来的事情就简单许多了。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def DFS(root):
            if not root:
                return 0, 0
            # 后序遍历
            leftchild_steal, leftchild_nosteal = DFS(root.left)
            rightchild_steal, rightchild_nosteal = DFS(root.right)

            # 偷当前node，则最大收益为【投当前节点+不偷左右子树】
            steal = root.val + leftchild_nosteal + rightchild_nosteal
            # 不偷当前node，则可以偷左右子树
            nosteal = max(leftchild_steal, leftchild_nosteal) + max(rightchild_steal, rightchild_nosteal)
            return steal, nosteal

        return max(DFS(root))