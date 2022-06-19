# Given the root of a binary tree, return the most frequent subtree sum.
# If there is a tie, return all the values with the highest frequency in any order.
#
# The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted
# at that node (including the node itself).
#

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def search(root):
            if not root:
                return 0
            root.val += search(root.left)
            root.val += search(root.right)
            result.append(root.val)
            return root.val

        result = list()
        search(root)
        count = Counter(result)
        max_time = count.most_common(1)[0][1]
        final_result = list()
        for line in count.most_common():
            if line[1] == max_time:
                final_result.append(line[0])
        return final_result

