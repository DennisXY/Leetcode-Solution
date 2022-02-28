# Given the head of a linked list, remove the nth node from the end of the list
# and return its head.
#
# Follow up: Could you do this in one pass?
# Example 1
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start = head
        length = 0
        while head:
            length += 1
            head = head.next
        head = start
        count = 0
        while count < length - n - 1:
            head = head.next
            count += 1
        if n == length:
            return start.next

        head.next = head.next.next
        return start