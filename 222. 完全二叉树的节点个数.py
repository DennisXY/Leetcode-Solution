# Given a complete binary tree, count the number of nodes.
#
# Note:
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
# are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

#O(n)
class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left+right+1

#Binary Search
class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        d = self.compute_depth(root)
        if d == 0:
            return 1
        left, right = 1, 2 ** d - 1
        while left <= right:
            mid = (left + right) // 2
            if self.exists(mid, d, root):
                left = mid + 1
            else:
                right = mid - 1

        return (2 ** d - 1) + left

    def compute_depth(self, node):
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx, d, node):
        left, right = 0, 2 ** d - 1
        for i in range(d):
            mid = (left + right) // 2
            if idx <= mid:
                right = mid - 1
                node = node.left
            else:
                left = mid + 1
                node = node.right
        return node is not None
