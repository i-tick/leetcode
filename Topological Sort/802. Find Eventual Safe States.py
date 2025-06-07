from collections import defaultdict, deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        def dfs(i):
            if i in safe:
                return safe[i]
            
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            safe[i] = True
            return True
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
    # time complexity: O(V + E) where V is the number of vertices and E is the number of edges
    # space complexity: O(V) for the safe dictionary and the recursion stack
    # This solution uses DFS to determine if a node is safe by checking if it can reach a cycle.
    # If it can reach a cycle, it is not safe; otherwise, it is safe.
    # The result is a list of all safe nodes in the graph.
    # The function returns a list of indices of the safe nodes in the graph.
    # The safe nodes are those that do not lead to a cycle in the directed graph.


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdeg = {}

        new_graph = defaultdict(list)
        for i, nodes in enumerate(graph):
            outdeg[i] = len(nodes)
            for node in nodes:
                new_graph[node].append(i)
        
        res = []
        q = deque()
        for i in outdeg:
            if outdeg[i] == 0:
                q.append(i)

        safe = [False] * len(graph)
        while q:
            node = q.popleft()
            safe[node] = True
            for nei in new_graph[node]:
                outdeg[nei] -= 1
                if outdeg[nei] == 0:
                    q.append(nei)
        res = []
        for i in range(len(graph)):
            if safe[i]:
                res.append(i)
        return res
    # time complexity: O(V + E) where V is the number of vertices and E is the number of edges
    # space complexity: O(V + E) for the new graph and outdeg dictionary
    # This solution uses Kahn's algorithm to perform a topological sort on the graph.
    # It builds a new graph with reversed edges and calculates the out-degrees of each node.
    # Nodes with zero out-degree are considered safe and added to the result list.
    # The function returns a list of indices of the safe nodes in the graph.
    # The safe nodes are those that do not lead to a cycle in the directed graph.


        
        