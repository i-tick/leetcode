from collections import defaultdict
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rank = defaultdict(int)
        par = {}

        # Union-Find with path compression and union by rank
        # Initialize parent array where each node is its own parent
        def find(i):
            if i!=par[i]:
                par[i] = find(par[i])
            return par[i]

        # Union operation to connect two nodes
        # If they are already connected, do nothing
        # If not, connect them and update the rank
        # to keep the tree flat
        def union(x,y):
            if x not in par:
                par[x] = x
            if y not in par:
                par[y] = y

            par_x = find(x)
            par_y = find(y)

            if rank[par_x] > rank[par_y]:
                par[par_y] = par_x
            elif rank[par_x] < rank[par_y]:
                par[par_x] = par_y
            else:
                par[par_y] = par_x
                rank[par_x] += 1


        offset = 100000
        # Union all stones in the same row or column
        # We use an offset to avoid negative indices
        for x, y in stones:
            union(x, (y + offset)) 
        # Find the number of unique groups
        # Each group represents a connected component of stones
        groups = set()
        # The number of stones that can be removed is the total number of stones minus the number of unique groups

        for key, val in par.items():
            # instead of using value, use find(key) to get the root of the group
            groups.add(find(key))
        print(par)
        return len(stones) - len(groups)
    
    # Time Complexity: O(n) where n is the number of stones.
    # Space Complexity: O(n) for the parent and rank dictionaries, where n is the number of stones.
    # The union-find operations are nearly constant time due to path compression and union by rank.
    # The overall complexity is efficient for the problem constraints, allowing for quick identification of the maximum number of stones that can be removed.
    # The function returns the maximum number of stones that can be removed, which is the total number of stones minus the number of unique groups formed by the union-find structure.
