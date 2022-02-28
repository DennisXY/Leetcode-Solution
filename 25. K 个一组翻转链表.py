# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        h, i = head, 1
        for i in range(k):
            if not h: return head
            h = h.next

        trail_reverse = head
        prev, next = None, head.next
        while head != h:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        head_reverse = prev
        trail_reverse.next = self.reverseKGroup(h, k)
        return head_reverse
