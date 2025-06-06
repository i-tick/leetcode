from collections import defaultdict
import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i, (u,v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        vis = set()

        pq = [(-1.0, start_node)]
        vis.add(start_node)
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end_node:
                return -cur_prob

            if graph[cur_node]:
                for neighbor, edge_prob in graph[cur_node]:
                    new_prob = -cur_prob * edge_prob
                    if new_prob > max_prob[neighbor] and neighbor not in vis:
                        max_prob[neighbor] = new_prob
                        heapq.heappush(pq, (-new_prob, neighbor))
                
        return 0