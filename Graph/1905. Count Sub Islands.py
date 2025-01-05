class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        R = len(grid2)
        C = len(grid2[0])

        vis = set()
        def dfs(r,c):
            if r<0 or c<0 or r>=R or c>=C or grid2[r][c]==0 or (r,c) in vis:
                return True

            vis.add((r,c))

            res = True

            if not grid1[r][c]:
                res = False

            res = dfs(r+1,c) and res
            res = dfs(r-1,c) and res
            res = dfs(r,c+1) and res
            res = dfs(r,c-1) and res

            return res


        c = 0
        for i in range(R):
            for j in range(C):
                if grid2[i][j] and (i,j) not in vis:
                    if dfs(i,j): c+=1
        return c

        