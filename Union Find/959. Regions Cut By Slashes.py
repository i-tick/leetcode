from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        N = 4*n*n
        par = [i for i in range(N)]
        rank = [1 for _ in range(N)]

        def find(i):
            if i!=par[i]:
                par[i] = find(par[i])
            return par[i]
        
        def union(n1,n2):
            par1 = find(n1)
            par2 = find(n2)

            if par1!=par2:
                if rank[par1] > rank[par2]:
                    par[par2] = par1
                elif rank[par1] < rank[par2]:
                    par[par1] = par2
                else:
                    par[par2] = par1
                    rank[par1] += 1
        # Union-Find structure to manage connected components in the grid
        # Each cell in the grid is represented by 4 nodes (top, right, bottom, left)
        # The grid is processed to union nodes based on the presence of slashes
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r * n + c)
            # if the box contains a "/" character, it will be partitioned into two regions. Therefore, we will merge the north-west and east-south regions to convert the box into two connected components.
                if val in '/ ': 
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)
            # If the box contains a "\" character, it will be partitioned into two regions. Therefore, we will merge the north-east and west-south regions to convert the box into two connected components.
                if val in '\ ':
                    union(root + 0, root + 2)
                    union(root + 1, root + 3)

            # The north region of the current box connects with the south region of the box above it.
            # The south region of the current box connects with the north region of the box below it.
            # The west region of the current box connects with the east region of the box to its left.
            # The east region of the current box connects with the west region of the box to its right
                if r+1 < n:
                    union(root + 3, (root + 4 * n) + 0)

                if r-1 >= 0:
                    union(root + 0, (root - 4 * n) + 3)
                
                if c+1 < n:
                    union(root + 2, (root + 4) + 1)

                if c-1 >= 0:
                    union(root + 1, (root - 4) + 2)
        return sum(find(x) == x for x in range(4 * n * n))
# Time Complexity: O(n^2 * log(n^2)) for union-find operations
# Space Complexity: O(n^2) for the parent and rank arrays, where n is the size of the grid.
# The union-find operations are nearly constant time due to path compression and union by rank.
# The overall complexity is efficient for the problem constraints, allowing for quick identification of the number of regions formed by slashes in the grid.
# The function returns the number of regions formed by slashes in the grid, where each region is defined by connected components of cells separated by slashes.
# The regions are counted by checking how many unique roots exist in the union-find structure after processing all cells in the grid.
# Example usage:
# sol = Solution()
# grid = [" /", "/ "]
# print(sol.regionsBySlashes(grid))  # Output: 2

