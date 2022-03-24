# Given the root of a binary tree and an integer targetSum,
# return the number of paths where the sum of the values 
# along the path equals targetSum.
#
# The path does not need to start or end at the root or a leaf,
# but it must go downwards (i.e., traveling only from parent nodes to child nodes).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def rootSum(root, target):
            if not root:
                return 0
            result = 0
            if root.val == target:
                result += 1
            result += rootSum(root.left, target-root.val)
            result += rootSum(root.right, target-root.val)
            return result
        if not root:
            return 0
        result = rootSum(root, targetSum)
        result += self.pathSum(root.left, targetSum)
        result += self.pathSum(root.right, targetSum)
        return result


# 方法二：前缀和 由根结点到当前结点的路径上所有节点的和
# 先序遍历二叉树，记录下根节点root到当前节点p的路径上除当前节点以外所有节点的前缀和
# 在已保存的路径前缀和中查找是否存在前缀和刚好等于当前节点到根节点的前缀和(curr)
# 减去targetSum

import collections


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0

            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)