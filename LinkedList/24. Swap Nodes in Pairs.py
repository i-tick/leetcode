# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        cur = head

        if not cur or not cur.next:
            return head

        while cur and cur.next:
            #labelling
            nex = cur.next.next
            second = cur.next

            #swap pairs
            second.next = cur
            cur.next = nex
            prev.next = second

            #move pointer
            prev = cur
            cur = nex

        return dummy.next
        