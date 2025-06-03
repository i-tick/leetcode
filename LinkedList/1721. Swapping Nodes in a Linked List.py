# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(next=head)
        pre_right = pre_left = None
        right = left = head
        # finds left node
        for i in range(k-1):
            pre_left = left
            left = left.next

        
        # finds right node
        # moves left node till end, so that right node is at k-th from end
        null_checker = left
        while null_checker.next:
            pre_right = right
            right = right.next
            null_checker = null_checker.next
            
        if left == right:
            return head
        
        # swap left and right nodes
        pre_left.next, pre_right.next = right, left
        left.next, right.next = right.next, left.next
        return dummy.next
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are swapping nodes in place without using extra space.
# Note: The function swaps the k-th node from the beginning with the k-th node from the end in a singly linked list.
# The function uses a dummy node to simplify edge cases and iteratively processes the linked list to find the nodes to be swapped.
# The main function first finds the k-th node from the beginning and then moves to the end of the list to find the k-th node from the end.
# Finally, it swaps the two nodes by adjusting the pointers accordingly and returns the modified list starting from the node after the dummy node.
# The final linked list is returned starting from the node after the dummy node.        