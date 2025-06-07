from collections import defaultdict, deque
from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_order = self.topological_sort(k, rowConditions)
        col_order = self.topological_sort(k, colConditions)

        if not row_order or not col_order:
            return []

        mat = [[0]*k for _ in range(k)]
        row_pos = {}
        for i, val in enumerate(row_order):
            row_pos[val] = i
        col_pos = {}
        for i, val in enumerate(col_order):
            col_pos[val] = i

        for num in range(1, k + 1):
            if num in row_pos and num in col_pos:
                mat[row_pos[num]][col_pos[num]] = num
        return mat


    def topological_sort(self, k, conditions):
        graph = defaultdict(list)
        indeg = {}
        for i in range(1, k+1):
            indeg[i] = 0
        for u,v in conditions:
            graph[u].append(v)
            indeg[v] += 1
        q = deque()
        for k in indeg:
            if indeg[k] == 0:
                q.append(k)
        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        if len(res)!=k:
            return []
        return res
# time complexity: O(k + m) where k is the size of the matrix and m is the number of nodes in the conditions
# space complexity: O(k + m) for the graph and indegree dictionary