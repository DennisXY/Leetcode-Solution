# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，返回null。

# 双指针第二次相遇的节点

class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
