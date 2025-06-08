# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], delete_nodes: List[int]) -> List[TreeNode]:
        # If the tree is empty, return an empty list.
        if not root:
            return []  

        to_delete = set(delete_nodes) 
        forest = []
        stack = [root]  # Use a stack to perform an iterative DFS.

        while stack:
            # Get the current node from the stack.
            node = stack.pop()  

            # Process the left child.
            if node.left:
                stack.append(node.left)  # Add the left child to the stack for further processing.
                if node.left.data in to_delete:  # If the left child needs to be deleted,
                    node.left = None  # Detach the left child from the current node.

            # Process the right child.
            if node.right:
                stack.append(node.right)  # Add the right child to the stack for further processing.
                if node.right.data in to_delete:  # If the right child needs to be deleted,
                    node.right = None  # Detach the right child from the current node.

            # If the current node itself needs to be deleted.
            if node.data in to_delete:
                if node.left:
                    forest.append(node.left)  # Add the left subtree to the forest if it exists.
                if node.right:
                    forest.append(node.right)  # Add the right subtree to the forest if it exists.

        # If the root node is not deleted, it becomes part of the forest.
        if root.data not in to_delete:
            forest.append(root)

        return forest  # Return the resulting forest as a list of tree roots.
    
    # Time complexity: O(n), where n is the number of nodes in the tree.
    # Space complexity: O(n), for the stack used in DFS and the forest list.
    # This solution efficiently traverses the tree and constructs the forest based on the deletion criteria.
    # It uses an iterative DFS approach to avoid recursion depth issues and handles the deletion of nodes while maintaining the structure of the remaining trees in the forest.
