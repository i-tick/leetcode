from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [0] * (len(edges) + 1)
        # Initialize parent array where each node is its own parent
        par = [i for i in range(len(edges)+1)]

        def find(n):
            p = par[n]

            if p!=n:
                return find(p)
            return p

        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1==p2:
                return False
            # par[max(p1,p2)]=min(p1,p2)
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        res = set()
        for i,j in edges:
            if not union(i,j):
                return [i,j]
# time complexity: O(n)
# space complexity: O(n) for the parent and rank arrays, where n is the number of edges.
# The union-find operations are nearly constant time due to path compression and union by rank.
# The overall complexity is efficient for the problem constraints, allowing for quick identification of the redundant connection in the graph.
# The function returns the first redundant connection it encounters, which is the last edge that would create a cycle in the graph.
# This is because the edges are processed in the order they are given, and the first edge that fails to union indicates a cycle.