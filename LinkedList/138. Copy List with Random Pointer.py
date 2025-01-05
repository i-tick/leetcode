"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {None:None}
        cur = head
        while cur:
            new_node = Node(cur.val)
            mapping[cur] = new_node
            cur = cur.next

        cur = head
        while cur:
            copy = mapping[cur]
            copy.next = mapping[cur.next]
            copy.random = mapping[cur.random]
            cur = cur.next
        return mapping[head]
        