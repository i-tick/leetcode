from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets):
            adj[src].append(dst)

        for src in adj:
            adj[src].sort(reverse=True)
        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
            
        dfs('JFK')
        return res[::-1]
# Time Complexity: O(e log e) due to sorting the tickets
# Space Complexity: O(e) for the adjacency list and the result list


