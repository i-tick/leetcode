# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        if not root:
            return False
        
        q = deque([root])
        seen = set()
        while q:
            node = q.popleft()
            if k - node.val in seen:
                return True
            seen.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
    # time complexity: O(n)
    # space complexity: O(n) for the queue and the set
    # where n is the number of nodes in the tree.