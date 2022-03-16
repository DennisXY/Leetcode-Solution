# Serialization is the process of converting a data structure or object
# into a sequence of bits so that it can be stored in a file or memory buffer,
# or transmitted across a network connection link to be reconstructed later
# in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization algorithm
# should work. You just need to ensure that a binary tree can be serialized
# to a string and this string can be deserialized to the original tree structure.
#

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ""

        def dfs_NLR(x: TreeNode) -> None:
            nonlocal res
            if x == None:
                res += 'None,'
                return
            else:
                res += str(x.val) + ','
                dfs_NLR(x.left)
                dfs_NLR(x.right)

        dfs_NLR(root)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        s = data.split(',')
        idx = 0

        def dfs_LRN() -> TreeNode:
            nonlocal idx
            if s[idx] == "None":
                idx += 1
                return None
            else:
                root = TreeNode(int(s[idx]))
                idx += 1
                root.left = dfs_LRN()
                root.right = dfs_LRN()
                return root

        return dfs_LRN()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
