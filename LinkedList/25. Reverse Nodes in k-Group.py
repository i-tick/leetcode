# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth_node = self.getKth(groupPrev, k)
            if not kth_node:
                break
            groupNext = kth_node.next

            newHead, newTail = self.reverseLinkedList(groupPrev.next, k)
            
            newTail.next = groupNext
            groupPrev.next = newHead
            groupPrev = newTail
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    def reverseLinkedList(self, head: Optional[ListNode],k) -> Optional[ListNode]:
        prev, nxt = None, None
        cur = head

        while k > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            k -= 1
        return prev, head  # return new head and tail
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are reversing in place without using extra space.
# Note: The function reverses nodes in k-group in a linked list, handling cases where the number of nodes is not a multiple of k by leaving the remaining nodes unchanged.
# The function uses a dummy node to simplify edge cases and iteratively processes each k-group, reversing the nodes in place.
# The helper function `getKth` finds the k-th node from the current position, and `reverseLinkedList` reverses the linked list segment of length k.
# The main function iterates through the linked list, reversing each k-group until there are no more complete groups left.
# The final linked list is returned starting from the node after the dummy node.