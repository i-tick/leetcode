class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return [[]]

        R = len(heights)
        C = len(heights[0])

        pac = set()
        atl = set()

        def backtrack(r,c,vis,val):
            if r<0 or c<0 or r>=R or c>=C or (r,c) in vis or heights[r][c]<val:
                return

            vis.add((r,c))
            backtrack(r-1,c,vis,heights[r][c])
            backtrack(r,c-1,vis,heights[r][c])
            backtrack(r,c+1,vis,heights[r][c])
            backtrack(r+1,c,vis,heights[r][c])


        for i in range(C):
            backtrack(0,i,pac,heights[0][i])
        for i in range(C):
            backtrack(R-1,i,atl,heights[R-1][i])
        for i in range(R):
            backtrack(i,0,pac,heights[i][0])
        for i in range(R):
            backtrack(i,C-1,atl,heights[i][C-1])

        res = []
        for r in range(R):
            for c in range(C):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
        