# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur = root
        new_node = TreeNode(val)

        while cur:
            if new_node.val>cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = new_node
                    break
            if new_node.val<=cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = new_node
                    break
        return root
        
        