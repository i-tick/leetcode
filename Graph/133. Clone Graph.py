
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}
        # Helper function to clone the graph using DFS
        # It uses a hashmap to keep track of already cloned nodes
        # to avoid cycles and ensure each node is cloned only once.
        # The function returns a new node that is a deep copy of the input node.
        def clone(node):
            if not node:
                return None
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))

            return copy

        return clone(node)
# Time Complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges (connections between nodes).
# Space Complexity: O(V), for the hashmap that stores the mapping from old nodes to new nodes.
# Note: The function clones a graph represented by nodes and their neighbors.
# It uses a depth-first search (DFS) approach to traverse the graph and create a deep copy of each node and its neighbors.
# The function maintains a mapping of old nodes to new nodes to avoid cycles and ensure each node is cloned only once.

        