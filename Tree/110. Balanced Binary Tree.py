# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isbalanced = 1
        def ht(root):
            nonlocal isbalanced
            if not root:
                return 0

            left = ht(root.left)
            right = ht(root.right)

            if abs(right-left)>1:
                isbalanced = 0

            print(root.val,1+max(right,left))
            return 1+max(right,left)

        ht(root)
        return isbalanced==1
        