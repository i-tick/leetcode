from collections import deque


class Solution(object):
    def minCost(self, grid):
        
        m, n = len(grid), len(grid[0])
        # Initialize the minCost matrix with a large value
        minCost = [[float('inf')] * n for _ in range(m)]
        minCost[0][0] = 0
        
        # Deque for 0-1 BFS
        # r,c = row, column
        dque = deque([(0, 0)])
        
        # Directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while dque:
            r, c = dque.popleft()
            
            # Visit adjacent cells
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                cost = 1 if grid[r][c] != i + 1 else 0
                
                if 0 <= nr < m and 0 <= nc < n and minCost[r][c] + cost < minCost[nr][nc]:
                    minCost[nr][nc] = minCost[r][c] + cost
                    
                    # Add to deque based on cost
                    if cost == 1:
                        dque.append((nr, nc))
                    else:
                        dque.appendleft((nr, nc))
        
        # Return the minimum cost to reach the bottom-right corner
        return minCost[m - 1][n - 1]
# time complexity: O(m * n)
# space complexity: O(m * n)
# m is the number of rows and n is the number of columns in the grid.
# The algorithm uses a deque for 0-1 BFS, which allows it to efficiently explore the grid while keeping track of the minimum cost to reach each cell.
# The minCost matrix is used to store the minimum cost to reach each cell, and it is updated as the algorithm explores the grid.
# The overall complexity is linear with respect to the number of cells in the grid, making it efficient for large grids.