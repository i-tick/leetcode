class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        R = len(board)
        C = len(board[0])
        vis = set()

        def dfs(r,c):
            nonlocal board
            if r not in range(R) or c not in range(C) or (r,c) in vis or board[r][c]!='O':
                return 
            board[r][c]='T'
            vis.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for i in range(R):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][C-1] == 'O':
                dfs(i,C-1)

        for i in range(C):
            if board[0][i] == 'O':
                dfs(0,i)
            if board[R-1][i] == 'O':
                dfs(R-1,i)
                
        for i in range(R):
            for j in range(C):
                if board[i][j]=='O':
                    board[i][j]='X'


        for i in range(R):
            for j in range(C):
                if board[i][j]=='T':
                    board[i][j]='O'

        