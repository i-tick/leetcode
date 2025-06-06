from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        n = len(edges)

        max_cycle = -1
        vis = [-1] * n
        time = 0

        for i in range(n):
            if vis[i] != -1:
                continue
            
            node_to_time = {}
            current = i

            # Traverse through the graph as long as:
            # - We haven't reached a dead end (current != -1)
            # - The node hasn't been globally visited yet
            while current != -1 and vis[current] == -1:
                # Mark the current node with the current global time
                node_to_time[current] = time
                vis[current] = time
                time += 1

                # Move to the next node in the path
                current = edges[current]

                # If we encounter a node we've already seen in this traversal,
                # we've found a cycle!
                if current in node_to_time:
                    # Calculate the length of the cycle
                    cycle_length = time - node_to_time[current]

                    # Update the maximum cycle length found so far
                    max_cycle = max(max_cycle, cycle_length)
                    break  # No need to go further in this path

        return max_cycle