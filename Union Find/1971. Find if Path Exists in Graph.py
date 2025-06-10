from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        par = [i for i in range(n)]

        def find(i):
            if i!=par[i]:
                par[i] = find(par[i])
            return par[i]

        def union(i,j):
            p1 = find(i)
            p2 = find(j)
            if p1!=p2:
                par[max(p1,p2)] = min(p1,p2)
        for i,j in edges:
            union(i,j)

        return find(source) == find(destination)
# Time Complexity: O(E + V) where E is the number of edges and V is the number of vertices.
# Space Complexity: O(V) for the parent array, where V is the number of vertices.
# The union-find operations are nearly constant time due to path compression, making the algorithm efficient for checking connectivity in the graph.
# The function returns True if there is a valid path from source to destination, and False otherwise.
# This is done by checking if both nodes have the same root in the union-find structure, indicating they are connected.
# The union-find structure efficiently groups connected components, allowing for quick path existence checks.
        