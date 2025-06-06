# A maze consists of n rooms numbered from 1 to n, and some rooms are connected by corridors. You are given a 2D integer array corridors where corridors[i] = [room1i, room2i] indicates that there is a corridor connecting room1i and room2i, allowing a person in the maze to go from room1i to room2i and vice versa.

# The designer of the maze wants to know how confusing the maze is. The confusion score of the maze is the number of different cycles of length 3.

# For example, 1 → 2 → 3 → 1 is a cycle of length 3, but 1 → 2 → 3 → 4 and 1 → 2 → 3 → 2 → 1 are not.
# Two cycles are considered to be different if one or more of the rooms visited in the first cycle is not in the second cycle.

# Return the confusion score of the maze.


# Input: n = 5, corridors = [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]]
# Output: 2
# Explanation:
# One cycle of length 3 is 4 → 1 → 3 → 4, denoted in red.
# Note that this is the same cycle as 3 → 4 → 1 → 3 or 1 → 3 → 4 → 1 because the rooms are the same.
# Another cycle of length 3 is 1 → 2 → 4 → 1, denoted in blue.
# Thus, there are two different cycles of length 3.

from collections import defaultdict
from typing import List

class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:

        graph = defaultdict(set)
        for u, v in corridors:
            graph[u].add(v)
            graph[v].add(u)

        count = 0
        for u in range(1, n + 1):
            for v in graph[u]:
                if v > u:
                    for w in graph[v]:
                        if w > v and w in graph[u]:
                            count += 1
        return count
# Time Complexity: O(n * d^2) where n is the number of rooms and d is the average degree of the nodes.
# Space Complexity: O(n + e) where n is the number of rooms and e is the number of corridors.
# Note: The function counts the number of unique cycles of length 3 in a maze represented by rooms and corridors.
# It constructs a graph from the corridors and iterates through each room to find cycles by checking connections with other rooms.
# The cycles are counted by ensuring that the rooms in the cycle are distinct and ordered.
# The final count of unique cycles is returned as the confusion score of the maze.


class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        graph = defaultdict(set)
        count = 0
        for u, v in corridors:
            graph[u].add(v)
            graph[v].add(u)

            count +=  len(graph[u].intersection(graph[v]))

        
        return count
# Time Complexity: O(n * e) where n is the number of rooms and e is the number of corridors.
# Space Complexity: O(n * n) where n is the number of rooms and e is the number of corridors.
# Note: The function counts the number of unique cycles of length 3 in a maze represented by rooms and corridors.
# It constructs a graph from the corridors and iterates through each room to find cycles by checking connections with other rooms.
# The cycles are counted by checking the intersection of neighbors of two connected rooms.
# The final count of unique cycles is returned as the confusion score of the maze.