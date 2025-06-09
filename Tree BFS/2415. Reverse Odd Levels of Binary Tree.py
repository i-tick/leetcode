# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        q = deque()
        q.append((root, 0))
        res = []
        res.append(root.val)
        while q:
            qlen = len(q)
            for _ in range(qlen):
                node, level = q.popleft()
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))
            if level%2==0:
                for i in range(len(q)//2):
                    q[i][0].val, q[len(q)-i-1][0].val = q[len(q)-i-1][0].val, q[i][0].val
        return root