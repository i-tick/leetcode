from collections import deque
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)

        in_degree = [0] * n
        for node in range(1, n):
            in_degree[parent[node]] += 1

        queue = deque()
        # Initialize the longest chains for each node
        # long_chains[node][0] = longest chain ending at node
        # long_chains[node][1] = second longest chain ending at node
        # This is used to track the two longest chains for each node
        long_chains = [[0, 0] for _ in range(n)]
        longest_path = 1

        for node in range(n):
            if in_degree[node] == 0:
                long_chains[node][0] = 1
                queue.append(node)

        # Process nodes in topological order
        # We will use a queue to process nodes with no incoming edges
        # and update the longest chains for their parents
        # This is a modified topological sort approach
        # where we also keep track of the longest paths
        # from each node to its parent nodes
        # and update the longest path accordingly
        while queue:
            current_node = queue.popleft()
            par = parent[current_node]

            # If the current node has a parent, we update the longest chains
            if par != -1:
                long_chain_from_current = long_chains[current_node][0]
                # If the current node has a different character than its parent,
                # we check if the longest chain from the current node
                # is longer than the longest chain ending at the parent node
                # If it is, we update the longest chains for the parent node
                # We also check if the second longest chain needs to be updated
                if s[current_node] != s[par]:
                    if long_chain_from_current > long_chains[par][0]:
                        long_chains[par][1] = long_chains[par][0]
                        long_chains[par][0] = long_chain_from_current
                    elif long_chain_from_current > long_chains[par][1]:
                        long_chains[par][1] = long_chain_from_current

                longest_path = max(longest_path, long_chains[par][0] + long_chains[par][1] + 1)

                in_degree[par] -= 1
                if in_degree[par] == 0:
                    long_chains[par][0] += 1
                    queue.append(par)
        
        return longest_path
    # time complexity: O(n)
    # space complexity: O(n)
    # where n is the number of nodes in the tree
    # This is because we process each node once and maintain a queue for processing nodes with no incoming edges.
    # The space complexity is also O(n) due to the storage of in-degrees and longest chains for each node.

