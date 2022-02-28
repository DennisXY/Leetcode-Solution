# Given a binary search tree (BST) with duplicates,
# find all the mode(s) (the most frequently occurred element) in the given BST.
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# For example:
# Given BST [1,null,2,2],
#
#    1
#     \
#      2
#     /
#    2
#
# return [2].
#
# Note: If a tree has more than one mode, you can return them in any order.
#
# Follow up: Could you do that without using any extra space?
# (Assume that the implicit stack space incurred due to recursion does not count).

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root):
        last = None
        Count = 0
        Max_Count = 0
        result = []

        def search(root: TreeNode):
            nonlocal Count, last, Max_Count, result
            if not root:
                return
            if root.left:
                search(root.left)
            if root.val == last:
                Count += 1
            else:
                Count = 1
            if Count == Max_Count:
                result.append(root.val)
            elif Count > Max_Count:
                result = list()
                result.append(root.val)
                Max_Count = Count
            last = root.val
            if root.right:
                search(root.right)
        search(root)
        return result


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    a.right = b
    b.left = c
    solution = Solution()
    c = solution.findMode(a)
    print(c)