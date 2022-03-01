# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list,
# we use an integer pos which represents the position (0-indexed)
# in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.


class Solution:
    def hasCycle(self, head) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast:
            if not fast.next:
                return False
            if slow == fast:
                return True
            fast = fast.next.next
            slow = slow.next
        return False