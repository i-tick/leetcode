from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indeg = {}
        for i in range(numCourses):
            indeg[i] = 0
        for v,u in prerequisites:
            graph[u].append(v)
            indeg[v] += 1
        
        q = deque()
        for k in indeg:
            if indeg[k] == 0:
                q.append(k)
        
        res = False
        course_taken = []
        # Perform topological sort using Kahn's algorithm
        # Process nodes with no incoming edges and reduce in-degrees of their neighbors
        # If a neighbor's in-degree becomes zero, add it to the queue
        while q:
            node = q.popleft()
            course_taken.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        # If we can process all nodes, we have a valid order
        # If not, return an empty list indicating a cycle or that not all nodes can be processed
        if len(course_taken) == numCourses:
            return course_taken
        return []