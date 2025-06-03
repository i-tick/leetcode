# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are modifying the list in place without using extra space.
# Note: The function removes duplicates from a sorted linked list, ensuring that each element appears only once.
# The function iterates through the linked list, checking for consecutive nodes with the same value and removing duplicates by adjusting pointers.
# The main function uses a while loop to traverse the list, and for each node, it checks if the next node has the same value.
# If it does, it skips the next node by adjusting the `next` pointer of the current node.
# The final linked list is returned starting from the head, with all duplicates removed.
# The function modifies the original list in place, and the final linked list is returned starting from the head.