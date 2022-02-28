# 合并k个已排序的链表并将其作为一个已排序的链表返回。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):

        length = len(lists)
        if length == 0:
            return lists
        if length == 1:
            return lists[0]

        mid = int(length / 2)
        left = length % 2

        l1 = lists[0:mid]
        l2 = lists[mid:2 * mid]
        r1 = self.mergeKLists(l1)
        r2 = self.mergeKLists(l2)
        r = self.merge2Lists(r1, r2)
        if left:
            r = self.merge2Lists(r, lists[-1])
        return r

    def merge2Lists(self, l1, l2):
        head = ListNode(0)
        r = head
        while l1 and l2:
            if l1.val < l2.val:
                r.next = l1
                l1 = l1.next
            else:
                r.next = l2
                l2 = l2.next
            r = r.next
        if l1:
            r.next = l1
        if l2:
            r.next = l2
        return head.next