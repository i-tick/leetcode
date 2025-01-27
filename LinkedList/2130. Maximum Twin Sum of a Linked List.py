# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # print(head.next)


        res = float('-INF')

        twin1 = head
        twin2 = prev
        while twin2:
            res = max(twin1.val+twin2.val,res)
            twin1 = twin1.next
            twin2 = twin2.next
        return res