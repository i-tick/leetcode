# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


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
        start.next = cur
        start_before.next = prev
        return dummy.next
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are reversing in place without using extra space.
# Note: The function reverses a segment of a linked list from position `left` to `right`, while leaving the rest of the list unchanged.
# The function uses a dummy node to simplify edge cases and iteratively processes the linked list to reverse the specified segment.
# The main function iterates through the linked list to find the starting point of the segment to be reversed, then reverses the segment in place.
# Finally, it connects the reversed segment back to the rest of the list and returns the modified list starting from the node after the dummy node.