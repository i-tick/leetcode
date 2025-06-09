from collections import defaultdict, deque
import math
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        graph1 = self.create_graph(edges1)
        graph2 = self.create_graph(edges2)

        node, _ = self.doBfs(0,graph1) # get the farthest node from 0 in graph1
        _, d1 = self.doBfs(node,graph1) # get the diameter of graph1

        node, _ = self.doBfs(0,graph2) # get the farthest node from 0 in graph2
        _, d2 = self.doBfs(node,graph2) # get the diameter of graph2

        # The minimum diameter after merging the two trees is the maximum of the two diameters,
        # plus the number of edges that would be added to connect the two trees.
        # The formula is max(d1, d2, ceil(d1/2) + ceil(d2/2) + 1)
        # This accounts for the longest path in each tree and the additional edges needed to connect them.
        # The +1 accounts for the edge that connects the two trees.
        # The ceil function is used to ensure that we round up when dividing the diameters by 2
        return max(d1,d2, math.ceil(d1/2) + math.ceil(d2/2) + 1) 
        # Time Complexity: O(n + m) where n and m are the number of edges in graph1 and graph2 respectively.
        # Space Complexity: O(n + m) for the graph representation using adjacency list.
        # The BFS traversal is O(n + m) as it visits each node and edge once.
        # The space complexity is O(n + m) for storing the graph in an adjacency list format.
        # The overall complexity is efficient for the problem constraints, allowing for quick computation of the minimum diameter after merging the two trees.
    
    def create_graph(self, edges):
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph
    
    def doBfs(self, startNode, graph):
        vis = set()
        q = deque([(startNode, 0)])

        while q:
            qlen = len(q)
            for _ in range(qlen):
                node, level = q.popleft()
                if node in vis:
                    continue
                vis.add(node)
                for nei in graph[node]:
                    q.append((nei, level +1))
        return node, level


