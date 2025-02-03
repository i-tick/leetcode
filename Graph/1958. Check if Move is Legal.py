class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        R = len(board)
        C = len(board[0])

        def dfs(r,c,rr,cc,col,vis):
            nr = r+rr
            nc = c+cc
            vis+=1
            

            if nr<0 or nc<0 or nr>=R or nc>=C or board[nr][nc]=='.':
                return False
            if board[nr][nc]==col:
                return vis>=3
            return dfs(nr,nc,rr,cc,col,vis)

        dirs = [[-1,0],[0,-1],[1,0],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
        for rr,cc in dirs:
            if dfs(rMove,cMove,rr,cc,color,1):
                return True
        return False
        