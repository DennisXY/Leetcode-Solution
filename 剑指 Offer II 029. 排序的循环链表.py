# 给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。
#
# 给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。
#
# 如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。
#
# 如果列表为空（给定的节点是 null），需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            head = node
            head.next = head
            return head
        elif head.next == head:
            head.next = node
            node.next = head
            return head

        curr = head
        next = head.next
        while next != head:
            if curr.val <= insertVal <= next.val:
                break
            if curr.val > next.val:
                if insertVal > curr.val or insertVal < next.val:
                    break
            curr = curr.next
            next = next.next
        curr.next = node
        node.next = next
        return head