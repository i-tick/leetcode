# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        cur = head
        prev = dummy
        # Iterate through the list
        while cur and cur.next:
            if cur.val == cur.next.val:
                # Move cur to the last duplicate
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                # Skip all duplicates by linking prev to the next unique value
                # prev.next will point to the next unique value after duplicates
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return dummy.next