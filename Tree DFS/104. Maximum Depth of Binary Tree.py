# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            nonlocal dep
            if not node:
                return 
            dep = max(dep, depth)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            return 
        dep = 0
        dfs(root, 1)
        return dep
