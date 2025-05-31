# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd_head =  ListNode(0)
        odd = odd_head
        even_head =  ListNode(0)
        even = even_head

        idx = 1
        while head:
            if idx ==1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            idx *=-1
        even.next = None
        odd.next = even_head.next

        return odd_head.next

        