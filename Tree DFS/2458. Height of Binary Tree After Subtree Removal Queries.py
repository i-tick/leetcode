# Definition for a binary tree node.
from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def tree_dfs(node, depth, depths, heights):
            if not node:
                return -1
            depths[node.val] = depth
            height = max(tree_dfs(node.left, depth + 1, depths, heights), tree_dfs(node.right, depth + 1, depths, heights)) + 1
            heights[node.val] = height
            return height

        depths = {}
        heights = {}
        tree_dfs(root, 0 , depths, heights)
        
        depth_group = defaultdict(list)
         # Group nodes by their depth. Keep the top 2 heights.
        for val, depth in depths.items():
            depth_group[depth].append((heights[val], val))
            depth_group[depth].sort(reverse=True)
            if len(depth_group[depth]) > 2:
                depth_group[depth].pop()
        res = []
        for q in queries:
            depth = depths[q]

            if len(depth_group[depth]) == 2:
                if depth_group[depth][0][1] == q:
                    # The removed node has the largest height, look for the node with 2nd largest height.
                    res.append(depth_group[depth][1][0] + depth)
                else:
                     # Look for the node with the largest height.
                    res.append(depth_group[depth][0][0] + depth)
            else:
                # No cousin, path length equals depth - 1.
                res.append(depth - 1)
        return res
