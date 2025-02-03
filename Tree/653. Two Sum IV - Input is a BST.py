# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def dfs(root,st,k):
            if not root:
                return False

            if k-root.val in st:
                return True
            st.add(root.val)
            return dfs(root.left,st,k) or dfs(root.right,st,k)

        st = set()
        return dfs(root,st,k)
        