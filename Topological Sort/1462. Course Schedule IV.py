# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

# Return a boolean array answer, where answer[j] is the answer to the jth query.
from collections import defaultdict, deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
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
        
        course_taken = []
        # Perform topological sort using Kahn's algorithm
        # Process nodes with no incoming edges and reduce in-degrees of their neighbors
        # If a neighbor's in-degree becomes zero, add it to the queue

        prereq = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        while q:
            node = q.popleft()
            course_taken.append(node)
            for nei in graph[node]:
            # Mark direct prerequisite
                prereq[nei][node] = True
                # Mark indirect prerequisites
                for k in range(numCourses):
                    if prereq[node][k]:
                        prereq[nei][k] = True
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        return [prereq[u][v] for u, v in queries]
    # Time complexity: O(n3 + m), where n is the number of courses and m is the number of prerequisites.
    # In Kahn's algorithm, we iterate over each node and edge of the vertex which is O(N 2) and for each edge traversed we 
    # will also add the prerequisites to the next node which is another O(N). To answer each query we need constant time to 
    # retrieve from the map and hence it's O(Q) to answer all queries. Hence, the total time complexity equals O(N 3+Q).   
    
    # Space complexity: O(n2 + m), where n2 is the space for the prerequisite matrix and m is for the queries.