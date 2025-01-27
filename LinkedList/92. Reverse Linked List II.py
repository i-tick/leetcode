# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        start_before = dummy
        start = head
        for i in range(left-1):
            start_before = start
            start = start.next
        
        prev = None
        cur = start
        # reverse from start till right
        for i in range(right-left+1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # assign back pointers
        start_before.next.next = cur
        start_before.next = prev
        return dummy.next
        