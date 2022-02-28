# # Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# #
# # Note: A leaf is a node with no children.
# #
# # Example:
# #
# # Given the below binary tree and sum = 22,
# #
# #       5
# #      / \
# #     4   8
# #    /   / \
# #   11  13  4
# #  /  \    / \
# # 7    2  5   1
# # Return:
# #
# # [
# #    [5,4,11,2],
# #    [5,8,4,5]
# # ]
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        ret = list()
        path = list()
        def dfs(root, total):

            if not root:
                return
            path.append(root.val)
            total -= root.val
            if not root.left and not root.right and total == 0:
                ret.append(path)
            dfs(root.left, total)
            dfs(root.right, total)
            path.pop()
        dfs(root, sum)
        return ret

# append(tmp)，等于是把tmp的地址接到了answer后面，tmp被修改，answer也被修改。
# 如果append(tmp[:])，就是answer后面新建了个list