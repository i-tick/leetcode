class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0]==1 or grid[N - 1][N - 1]==1:
            return -1

        q = deque()
        q.append((0,0,0))
        vis = set((0,0))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]
        while q:
            r,c,l = q.popleft()


            if r== N-1 and c==N-1:
                return l+1


            for i,j in dirs:
                nr = r+i
                nc = c+j
                if (nr,nc) not in vis and 0<=nr<N and 0<=nc<N and grid[nr][nc]!=1:
                    q.append((nr,nc,l+1))
                    vis.add((nr,nc))
        return -1
        