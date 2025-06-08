# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderidx = {v:i for i,v in enumerate(inorder)}

        def dfs(l,r):
            while l>r:
                return None
            root = TreeNode(postorder.pop())
            idx = inorderidx[root.val]
            root.right = dfs(idx+1,r)
            root.left = dfs(l,idx-1)
            return root

        return dfs(0,len(inorder)-1)
        