# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        t = ListNode(0, head)
        f = t
        l = head

        # take right pointer n node ahead
        while n>0:
            l = l.next
            n-=1
        
        # now left and right pointer are n nodes apart
        # traverse each node untill right pointer is at end
        while l:
            l = l.next
            f = f.next

        # once right is at end, left is n nodes before
        f.next = f.next.next

        return t.next
        