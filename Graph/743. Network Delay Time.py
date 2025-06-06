import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        # Build the graph as an adjacency list
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        # Use a min-heap to perform Dijkstra's algorithm
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1
# Time Complexity: O((n + e) log n) where n is the number of nodes and e is the number of edges.
# Space Complexity: O(n + e) for the graph representation and the min-heap.
# Note: The function implements Dijkstra's algorithm to find the shortest path from a starting node k to all other nodes in a directed graph.
# It returns the time it takes for a signal to reach all nodes, or -1 if not all nodes are reachable.
# The graph is represented as an adjacency list, and a min-heap is used to efficiently get the next node with the smallest distance.
# The algorithm iteratively updates the shortest known distances to each node until all reachable nodes are visited.
# The final time is returned if all nodes are reachable; otherwise, -1 is returned.
# The function returns the time it takes for a signal to reach all nodes, or -1 if not all nodes are reachable.
# The graph is represented as an adjacency list, and a min-heap is used to efficiently get the next node with the smallest distance.