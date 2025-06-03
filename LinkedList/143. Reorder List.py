# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find center of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        # reverse 2nd list
        cur = second
        while cur:
            nxt = cur.next
            second.next = prev
            prev = cur
            cur = nxt

        # merge both the list
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1, tmp2

        return head
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are rearranging the nodes in place without using extra space.
# Note: The function reorders a linked list in a specific pattern: first node, last node, second node, second last node, and so on.
# The function first finds the middle of the linked list, then reverses the second half, and finally merges the two halves in the required order.
# The main function uses two pointers to find the middle of the list, reverses the second half, and then merges the two halves by alternating nodes from each half.
# The final linked list is modified in place, and the function does not return anything as it modifies the original list.