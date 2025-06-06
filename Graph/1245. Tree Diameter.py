# 1245. Tree Diameter

# The diameter of a tree is the number of edges in the longest path in that tree.

# There is an undirected tree of n nodes labeled from 0 to n - 1. You are given a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the tree.

# Return the diameter of the tree.

# Input: edges = [[0,1],[0,2]]
# Output: 2
# Explanation: The longest path of the tree is the path 1 - 0 - 2.

# Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
# Output: 4
# Explanation: The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
 

from collections import defaultdict
from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        vis = set()
        diameter = [0]

        def dfs(node: int, parent: int):
            vis.add(node)
            max_depth = 0
            second_max_depth = 0
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                depth = dfs(neighbor, node) + 1

                if depth > max_depth:
                    second_max_depth = max_depth
                    max_depth = depth
                elif depth > second_max_depth:
                    second_max_depth = depth
                    
            diameter[0] = max(diameter[0], max_depth + second_max_depth)
            return max_depth
        
        dfs(0, -1)
        return diameter[0]
    # end of class Solution
    # time complexity: O(n)
    # space complexity: O(n)