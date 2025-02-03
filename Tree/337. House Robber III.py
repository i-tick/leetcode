# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = { None : 0 }
        def dfs(root):
            if not root:
                cache[root] = 0
                return 0

            if root in cache:
                return cache[root]
            # taking root or without taking root
            # taking root + left (skip root.left) + right (skip root.right)
            cache[root] = root.val
            if root.left:
                cache[root]+= dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                cache[root]+= dfs(root.right.left) + dfs(root.right.right)
            
            # return max(res or root.left+root.right)
            cache[root] = max(cache[root], dfs(root.left)+ dfs(root.right))
            return cache[root]
        return dfs(root)
            