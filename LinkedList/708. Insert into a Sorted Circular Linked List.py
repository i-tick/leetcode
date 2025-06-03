# Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

# If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

# If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.


# Input: head = [3,4,1], insertVal = 2
# Output: [3,4,1,2]
# Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.



# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            node.next = node
            return node
        
        prev = head
        cur = head.next
        flag = False

        while cur!=head:
            if prev.val<= insertVal <= cur.val:
                flag = True

            elif prev.val > cur.val:
                if insertVal >= prev.val or insertVal <= cur.val:
                    flag = True

            if flag:
                prev.next = Node(insertVal, cur)
                return head

            prev, cur = cur, cur.next

        # If we reach here, it means we didn't find a suitable place to insert
        # if list contains only one element or if all elements are the same
        # if all the elements are the same, we can insert at the end
        prev.next = Node(insertVal, cur)
        return head