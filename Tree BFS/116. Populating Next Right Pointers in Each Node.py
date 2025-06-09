# Definition for a Node.
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)-1):
                q[i].next = q[i+1]
            q[-1].next=None

            for _ in range(len(q)):
                node = q.popleft()
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)

        return root
    # Time Complexity: O(n)
    # Space Complexity: O(n) for the queue, where n is the number of nodes in the tree.
        