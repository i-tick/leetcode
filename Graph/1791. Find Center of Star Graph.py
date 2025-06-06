from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first_edge = edges[0]
        second_edge = edges[1]

        if first_edge[0] in second_edge:
            return first_edge[0]
        else:
            return first_edge[1]
# # Time Complexity: O(1) since we only check the first two edges
# # Space Complexity: O(1) as we are not using any additional data structures
# # Note: The function assumes that the input edges form a star graph, where one node is connected to all others.
# #       It returns the center node of the star graph, which is the node that appears in both of the first two edges.
# #       The function is efficient because it only inspects the first two edges, which is sufficient to determine the center in a star graph.
# #       The function does not need to traverse the entire graph, making it very efficient for this specific problem.