# Given the root of a binary tree, return the postorder traversal of its nodes' values.
#
# Example 1:
#
# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
# Example 4:
#
#
# Input: root = [1,2]
# Output: [2,1]
# Example 5:
#
# Input: root = [1,null,2]
# Output: [2,1]
# Constraints:
#
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
# Follow up:
# Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Recursive
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def bfs(root: TreeNode):
            if not root:
                return
            bfs(root.left)

            bfs(root.right)
            result.append(root.val)

        bfs(root)
        return result

#Without Recursive, Using Iterative
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []   # 用来存储后序遍历节点的值
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)  # 第一次入栈的是根节点
                #判断当前节点的左子树是否存在，若存在则持续左下行，若不存在就转向右子树
                node = node.left if node.left is not None else node.right
            #循环结束说明走到了叶子节点，没有左右子树了，该叶子节点即为当前栈顶元素，应该访问了
            node = stack.pop() # 取出栈顶元素进行访问
            res.append(node.val) # 将栈顶元素也即当前节点的值添加进res
            # （下面的stack[-1]是执行完上面那句取出栈顶元素后的栈顶元素）
            if stack and stack[-1].left == node: # 若栈不为空且当前节点是栈顶元素的左节点
                node = stack[-1].right   # 则转向遍历右节点
            else:
                node = None  # 没有左子树或右子树，强迫退栈
        return res
