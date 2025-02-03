# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nodes = []

        def inorder(node):
            # nonlocal res
            if not node:
                return
            cur  = node
            inorder(cur.left)
            nodes.append(cur.val)
            inorder(cur.right)

        inorder(root)
        ans = float('INF')
        for i in range(len(nodes)-1):
            ans = min(ans,nodes[i+1]-nodes[i])
        return ans

        