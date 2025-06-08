# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        # Flatten the tree in-place by rearranging the nodes
        while cur:
            # If the current node has a left child, find the rightmost node of the left subtree
            # and attach the right subtree to it
            # Then move the left subtree to the right and set left to None
            if cur.left:
                last = cur.left
                while last.right:
                    last = last.right
                
                last.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

        return cur

        