# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root

        def BFS(oneLayer):
            nextLayer = []  # 每一次都搞个空的列表，去建立nextLayer
            for i in oneLayer:
                if i.left:
                    nextLayer.append(i.left)
                if i.right:
                    nextLayer.append(i.right)

            if len(nextLayer) > 1:  # 一共只有1个节点就没必要搞了。
                for j in range(0, len(nextLayer) - 1):
                    nextLayer[j].next = nextLayer[j + 1]  # 每个节点的next指向后面一个节点。

            if nextLayer:  # nextLayer不是空的话就继续往下走。
                BFS(nextLayer)

        BFS([root])  # 最开始就是只有一层一个根节点。
        return root

