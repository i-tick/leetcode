# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def ht_dfs(root):
            nonlocal diameter
            if not root:
                return 0
            left = ht_dfs(root.left)
            right = ht_dfs(root.right)
            
            diameter = max(diameter,left+right)

            return 1+max(left,right)

        ht_dfs(root)
        return diameter
        