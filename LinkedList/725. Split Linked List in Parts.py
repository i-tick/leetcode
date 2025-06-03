# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import math
from typing import Optional
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        cur = head
        while cur:
            cur = cur.next
            l+=1
        n, r = divmod(l, k)
        cur = head
        prev = None
        res = [None] * k

        for i in range(k):
            res[i] = cur

            # Move cur to the end of the current part, 
            # for the first part, it will have n + 1 nodes if r > 0
            if r>0:
                r-=1
                for i in range(n+1):
                    prev = cur
                    cur = cur.next
            else:
                for i in range(n):
                    prev = cur
                    cur = cur.next
            
            if prev:
                prev.next = None

        return res
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(k), where k is the number of parts to split the linked list into.
# Note: The function splits a linked list into k parts, distributing nodes as evenly as possible.
# The function first calculates the length of the linked list, then determines the size of each part and how many parts will have an extra node.
# It iterates through the linked list, creating parts and adjusting pointers to separate the parts.
# The final result is a list of linked list heads, where each part is represented by its head node.
# The function returns a list of linked list heads, where each part is represented by its head node.