# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        if root==p:
            return p
        if root==q:
            return q

        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)

        if l and r:
            return root

        if l:
            return l
        else:
            return r
        # time complexity: O(n)
        # space complexity: O(h) where h is the height of the tree, due to recursion stack
        # This solution uses a recursive depth-first search (DFS) to find the lowest common ancestor of two nodes in a binary tree.
        # It checks if the current node is one of the target nodes (p or q), and if so, returns that node.
        # If not, it recursively searches the left and right subtrees.
        # If both left and right recursive calls return non-null values, it means the current node is the lowest common ancestor.
        # If only one of the recursive calls returns a non-null value, it means that the ancestor is in that subtree.
        # If both calls return null, it means neither p nor q is found in that subtree, and the function returns null.
        