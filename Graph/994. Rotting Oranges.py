class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])
        time = 0

        q = deque()
        def bfs():
            nonlocal time
            while q:
                flag = 0
                for _ in range(len(q)):
                    row,col = q.popleft()
                    dirs = [[-1,0],[1,0],[0,1],[0,-1]]
                    for dirr,dirc in dirs:
                        r = row+dirr
                        c = col+dirc
                        if r not in range(R) or c not in range(C) or grid[r][c]!=1:
                            continue
                        flag =1
                        grid[r][c]=2
                        q.append((r,c))
                if flag:
                    time+=1


        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2 and (i,j):
                    q.append((i,j))
        bfs()
        
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    return -1
        return time
        