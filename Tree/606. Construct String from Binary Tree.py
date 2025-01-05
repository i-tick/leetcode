# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        res = []
        def preorder(root):
            if not root:
                return 
            res.append('(')
            res.append(str(root.val))

            # if left node is empty but not right, we need ()
            # if left node is not empty but right is, we dont need ()
            # try with an example
            if not root.left and root.right:
                res.append('()')
            
            preorder(root.left)
            preorder(root.right)
            res.append(')')
        
        preorder(root)
        return "".join(res[1:-1]) # mot taking first and last ( )
            
        