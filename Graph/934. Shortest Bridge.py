class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])
        visit = set()
        def dfs(r,c):
            if r not in range(R) or c not in range(C) or grid[r][c]!=1 or (r,c) in visit:
                return 

            visit.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)


        def bfs():
            q = deque(visit)
            res = 0

            while q:
                for _ in range(len(q)):
                    r,c  = q.popleft()
                    direct = [[-1,0],[1,0],[0,1],[0,-1]]
                    for dirr,dirc in direct:
                        row = r+dirr
                        col = c+dirc
                        if row not in range(R) or col not in range(C) or (row,col) in visit:
                            continue
                        if grid[row][col]==1:
                            return res
                        visit.add((row,col))
                        q.append((row,col))
                res+=1
            return res
        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs()
        
        