from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check for cycle
        if len(edges)>(n-1) or len(edges)<(n-1):
            return False
        
        # build neighbour list
        neigh = defaultdict(list)
        for i,j in edges:
            neigh[i].append(j)
            neigh[j].append(i)


        #check if all nodes are connected
        vis = set()
        def dfs(n,par):
            vis.add(n)
            for i in neigh[n]:
                if i==par or i in vis:
                    continue
                dfs(i,n)
        dfs(0,-1)
        return len(vis)==n
# Time Complexity: O(n) where n is the number of nodes and m is the number of edges
# Space Complexity: O(n + m) for the adjacency list representation of the graph
# Note: The function checks if a given undirected graph is a valid tree by ensuring it has exactly n-1 edges and that all nodes are connected.
# It uses Depth First Search (DFS) to traverse the graph and mark visited nodes, ensuring that all nodes are reachable from the starting node.
# If the number of edges is not equal to n-1 or if not all nodes are visited after the DFS traversal, the function returns False, indicating that the graph is not a valid tree.
# If both conditions are satisfied, it returns True, indicating that the graph is a valid tree.