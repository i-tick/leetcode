# DFS
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        R = len(grid)
        C = len(grid[0])
        island = 0
        vis = set()
        def dfs(r,c):
            if r<0 or c<0 or r>=R or c>=C or grid[r][c]=='0' or (r,c) in vis:
                return

            vis.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            return True

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1' and (i,j) not in vis:
                    if dfs(i,j):
                        island+=1

        return island

# BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        R = len(grid)
        C = len(grid[0])
        island = 0
        vis = set()

        def bfs(r,c):
            q = deque()
            vis.add((r,c))
            q.append((r,c))

            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    dir = [[1,0], [-1,0], [0,1], [0,-1]]
                    for dr,dc in dir:
                        r = row + dr
                        c = col + dc

                        if (r in range(R) and c in range(C) and grid[r][c] == '1' and (r,c) not in vis):
                            q.append((r,c))
                            vis.add((r,c))

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1' and (i,j) not in vis:
                    # print(i,j,vis)
                    bfs(i,j)
                    island+=1

        return island
# Time Complexity: O(R * C) where R is the number of rows and C is the number of columns in the grid.   
# Space Complexity: O(R * C) for the visited set and the queue in the BFS approach, where R is the number of rows and C is the number of columns in the grid.
# The DFS approach has a similar time complexity but uses the call stack for recursion, which can also lead to O(R * C) space complexity in the worst case.
# Both approaches efficiently traverse the grid to count the number of islands, ensuring that each cell is processed only once.
# The BFS approach uses a queue to explore all connected '1's, while the DFS approach uses recursion to achieve the same result.
# Both methods ensure that all parts of an island are visited before moving on to the next unvisited '1'.
# The choice between BFS and DFS can depend on personal preference or specific constraints of the problem, but both will yield the same result in this case.




class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rank = []
        par = []
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    par.append(i*n + j)
                    count += 1
                else:
                    par.append(-1)
                rank.append(0)
        

        def find(i):
            if par[i] != i:
                par[i] = find(par[i])
            return par[i]

        def union(i,j):
            nonlocal count
            par_i = find(i)
            par_j = find(j)

            if par_i!=par_j:
                if rank[par_i] > rank[par_j]:
                    par[par_j] = par_i
                elif rank[par_i] < rank[par_j]:
                    par[par_i] = par_j
                else:
                    par[par_j] = par_i
                    rank[par_i] += 1
                count -= 1
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    grid[r][c] = "0"

                    if c+1<n and grid[r][c+1] == "1":
                        union(r*n + c, r*n+(c+1))    
                    if r+1<m and grid[r+1][c] == "1":
                        union(r*n + c, ((r+1)*n)+c)
        return count
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n) for the parent and rank arrays, where m is the number of rows and n is the number of columns in the grid.
    # The union-find operations are nearly constant time due to path compression and union by rank.
    # The overall complexity is efficient for the problem constraints, allowing for quick identification of the number of islands in the grid.
    # The function returns the number of islands, which is the number of connected components in the grid where '1's represent land and '0's represent water.