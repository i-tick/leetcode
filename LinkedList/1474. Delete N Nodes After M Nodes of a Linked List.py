# You are given the head of a linked list and two integers m and n.

# Traverse the linked list and remove some nodes in the following way:

# Start with the head as the current node.
# Keep the first m nodes starting with the current node.
# Remove the next n nodes
# Keep repeating steps 2 and 3 until you reach the end of the list.
# Return the head of the modified list after removing the mentioned nodes.

#  Example 1:


# Input: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
# Output: [1,2,6,7,11,12]
# Explanation: Keep the first (m = 2) nodes starting from the head of the linked List  (1 ->2) show in black nodes.
# Delete the next (n = 3) nodes (3 -> 4 -> 5) show in read nodes.
# Continue with the same procedure until reaching the tail of the Linked List.
# Head of the linked list after removing nodes is returned.

 # Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def traverse(self, head, k):
        cur = head
        prev = None
        while cur and k>0:
            prev = cur
            cur = cur.next
            k-=1
        return prev
        

    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy = head
        while dummy:
            # Keep the first m nodes
            group_end = self.traverse(dummy, m)
            dummy = group_end.next
            last_node = group_end
            if dummy:
                # Remove the next n nodes
                group_end = self.traverse(dummy, n)
                last_node.next = group_end.next
                dummy = group_end.next
                last_node = dummy
        return head
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are modifying the list in place without using extra space.
# Note: The function deletes nodes in a linked list based on the given m and n values.
# The function iterates through the linked list, keeping the first m nodes and removing the next n nodes repeatedly until the end of the list is reached.
# The helper function `traverse` is used to move through the linked list and return the last node of the current group.
# The main function uses a dummy node to simplify edge cases and iteratively processes the linked list.
# The final linked list is returned starting from the original head.