class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])

        visit = set()

        def dfs(r,c):
            if r not in range(R) or c not in range(C) or grid[r][c]==0 or (r,c) in visit:
                return 0
            
            visit.add((r,c))
            return (1+dfs(r-1,c) + dfs(r+1,c) + dfs(r,c+1) + dfs(r,c-1))

        max_area = float('-inf')

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1 and (i,j) not in visit:
                    max_area = max(max_area,dfs(i,j))

        return 0 if max_area == float('-inf') else max_area
        