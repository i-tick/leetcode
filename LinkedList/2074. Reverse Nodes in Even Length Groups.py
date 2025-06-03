# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = head
        group_size = 1
        prev_group_end = dummy
        prev_cur = None

        while cur:
            group_start = cur
            count = 0
            
            # Count the number of nodes in the current group
            while cur and count < group_size:
                count += 1
                cur = cur.next
            
            # If the group has an even length, reverse it
            if count % 2 == 0:
                prev, current = None, group_start
                for _ in range(count):
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
                
                # Connect the reversed group back to the list
                prev_group_end.next = prev
                prev_group_end = group_start
                group_start.next = cur
            else:
                # If the group has an odd length, do not reverse it
                for _ in range(count):
                    prev_group_end = prev_group_end.next
                
            # Move to the next group size
            group_size += 1
        
        return dummy.next
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are rearranging the nodes in place without using extra space.
# Note: The function reverses nodes in even-length groups in a linked list, while leaving odd-length groups unchanged.
# The function uses a dummy node to simplify edge cases and iteratively processes the linked list in groups.
# The main function iterates through the linked list, counting nodes in each group and reversing the group if it has an even length.
# The final linked list is returned starting from the node after the dummy node.
# The function modifies the original list in place, and the final linked list is returned starting from the node after the dummy node.