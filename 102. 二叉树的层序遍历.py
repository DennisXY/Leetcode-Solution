# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return list()
        stack, result = [root], list()
        while len(stack) > 0:
            temp = [i.val for i in stack]
            temp_stack = list()
            for i in stack:
                if i.left:
                    temp_stack.append(i.left)
                if i.right:
                    temp_stack.append(i.right)
            stack = temp_stack
            result.append(temp)
        return result

