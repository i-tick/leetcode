# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # got till mid
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse from mid
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # traverse from both end. If all equal palindrome
        left,right = head, prev
        while right:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next

        return True
        