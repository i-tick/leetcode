# DFS
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
        