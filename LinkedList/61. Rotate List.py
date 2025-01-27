# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or not head:
            return head

        l=1
        # find length
        tail = head
        while tail.next:
            tail = tail.next
            l+=1
        k = k%l

        if k==0:
            return head
        
        cur = head
        print(k,l)
        for i in range(l-k-1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        tail.next = head
        return new_head

        