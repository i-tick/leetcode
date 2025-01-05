class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        R = len(grid)
        C = len(grid[0])


        def bfs(r,c,dis):
            q = deque()
            vis.add((r,c))
            q.append((r,c))

            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    dir = [[1,0], [-1,0], [0,1], [0,-1]]
                    grid[row][col] = min(dis,grid[row][col])
                    for dr,dc in dir:
                        r = row + dr
                        c = col + dc

                        if (r in range(R) and c in range(C) and grid[r][c] != -1 and (r,c) not in vis):
                            q.append((r,c))
                            vis.add((r,c))
                dis+=1

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    vis = set()
                    bfs(i,j,0)