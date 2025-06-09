# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res
        
        # res = []
        # if not root:
        #     return []
        # cur = root
        # while cur:
        #     if cur.left is None:
        #         res.append(cur.val)
        #         cur = cur.right
        #     else:
        #         prev = cur.left
        #         while prev.right is not None and prev.right!=cur:
        #             prev = prev.right
        #         if prev.right==None:
        #             prev.right = cur
        #             cur = cur.left
        #         else:
        #             prev.right = None
        #             res.append(cur.val)
        #             cur = cur.right
    
        # return res

        # Time complexity: O(n)