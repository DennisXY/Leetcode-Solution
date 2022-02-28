# 给出两个非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式
# 存储的，并且它们的每个节点只能存储一位数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        r = ListNode(0)
        result = r
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s//10
            r.next = ListNode(s%10)
            r = r.next
            if not l1:
                l1 = l1.next
            if not l2:
                l2 = l2.next
        if carry:
            r.next=ListNode(1)
        return result.next


# 方法2， 不创建新的链表，直接在上面相加
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        temp_head = l1
        l1_prev = None
        while l1 and l2:
            if l1.val + l2.val + carry > 9:
                l1.val = (l1.val + l2.val + carry) % 10
                carry = 1
            else:
                l1.val = l1.val + l2.val + carry
                carry = 0
            l1_prev = l1
            l1 = l1.next
            l2 = l2.next
        if not l1:
            if not l2 and carry:
                l1_prev.next = ListNode(carry)
            else:
                l1_prev.next = l2
            while l2:
                if l2.val + carry > 9:
                    l2.val = (l2.val + carry) % 10
                    carry = 1
                    if not l2.next:
                        l2.next = ListNode(1)
                        break
                    l2 = l2.next

                else:
                    l2.val += carry
                    carry = 0
                    break
        else:
            while l1:
                if l1.val + carry > 9:
                    l1.val = (l1.val + carry) % 10
                    carry = 1
                    if not l1.next:
                        l1.next = ListNode(1)
                        break
                    l1 = l1.next
                else:
                    l1.val += carry
                    carry = 0
                    break

        return temp_head



