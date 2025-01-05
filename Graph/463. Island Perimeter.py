class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        vis = set()
        R = len(grid)
        C = len(grid[0])
        p = 0
        def dfs(i,j):
            nonlocal p
            l,r,b,t = 0,0,0,0
            if i<0 or j<0 or i>=R or j>=C or grid[i][j]==0:
                return 1
            if (i,j) in vis:
                return 0
            
            vis.add((i,j))
            b = dfs(i+1,j)
            r = dfs(i,j+1)
            l = dfs(i,j-1)
            t = dfs(i-1,j)

            p += l + r + b + t
            return 0
            
        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    dfs(i,j)
                    return p
        