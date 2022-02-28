# Given the root of a binary tree, flatten the tree into a "linked list":
#
# The "linked list" should use the same TreeNode class
# where the right child pointer points to the next node in the list
# and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal
# of the binary tree.

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        tree_list = list()
        def preorder(root):
            if not root:
                return
            tree_list.append(root)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        new_root = tree_list[0]
        return_root = tree_list[0]
        for i in tree_list[1:]:
            new_root.left = None
            new_root.right = i
            new_root = new_root.right
        return return_root


# 不用额外的空间：官方解答。看video
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/
class Solution:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right
