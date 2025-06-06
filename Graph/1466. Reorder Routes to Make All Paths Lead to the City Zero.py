from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        vis = set()
        neighbors = defaultdict(list)
        for a,b in connections:
            neighbors[a].append((b,1))
            neighbors[b].append((a,0))

        print(neighbors)
        vis = set()
        result = [0]
        def dfs(node, neighbors, vis):
            vis.add(node)
            for nei, need_to_reverse in neighbors[node]:
                if nei not in vis:
                    result[0] += need_to_reverse
                    dfs(nei, neighbors, vis)
            return result[0]
        dfs(0, neighbors, vis)
        return result[0]