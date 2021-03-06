# Given a linked list and a value x, partition it such that
# all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes
# in each of the two partitions.
#
# Example:
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p = first = ListNode(0)
        q = second = ListNode(0)
        while head:
            if head.val < x:
                first.next = head
                first = first.next
            else:
                second.next = head
                second = second.next
            head = head.next

        second.next = None
        first.next = q.next
        return p.next