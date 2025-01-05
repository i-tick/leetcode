# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        prev = res

        carry = 0
        if not l1:
            return l2
        if not l2:
            return l1

        
        while l1 and l2:
            if l1 and l2:
                res.next = ListNode((l1.val + l2.val + carry)%10)
                carry = (l1.val + l2.val + carry)//10
                l1 = l1.next
                l2 = l2.next
                res = res.next

        while l1:
            res.next = ListNode((l1.val + carry)%10)
            carry = (l1.val + carry)//10
            l1 = l1.next
            res = res.next
        while l2:
            res.next = ListNode((l2.val + carry)%10)
            carry = (l2.val + carry)//10
            l2 = l2.next
            res = res.next

        if carry:
            res.next = ListNode(carry)
        return prev.next