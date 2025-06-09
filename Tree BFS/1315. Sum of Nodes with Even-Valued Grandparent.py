# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 0)])
        res = 0
        while q:
            qlen = len(q)
            for _ in range(qlen):
                node, level = q.popleft()
                if node.left:
                    if node.left.left and node.val%2 == 0:
                        res+=node.left.left.val
                    if node.left.right and node.val%2 == 0:
                        res+=node.left.right.val
                    q.append((node.left, level +1))
                if node.right:
                    if node.right.left and node.val%2 == 0:
                        res+=node.right.left.val
                    if node.right.right and node.val%2 == 0:
                        res+=node.right.right.val
                    q.append((node.right, level +1))
        return res