# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1 and not root2:
            return None

        if not root1:
            v1 = 0
            left1 = None
            right1 = None
        else:
            v1 = root1.val
            left1 = root1.left
            right1 = root1.right
            
        if not root2:
            v2 = 0
            left2 = None
            right2 = None
        else:
            v2 = root2.val
            left2 = root2.left
            right2 = root2.right

        root = TreeNode(v1+v2)

        root.left = self.mergeTrees(left1, left2)
        root.right = self.mergeTrees(right1,right2)

        return root