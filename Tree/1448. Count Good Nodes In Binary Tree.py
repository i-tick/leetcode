# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        result = 0
        def dfs(node,maxVal):
            nonlocal result
            if not node:
                return 0


            if node.val>=maxVal:   
                res =  1
            else:
                res =  0

            maxVal = max(maxVal, node.val)
            res += dfs(node.left,maxVal)
            res += dfs(node.right, maxVal)
            print(res)

            return res
        return dfs(root,root.val)
        