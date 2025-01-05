class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        R = len(board)
        C = len(board[0])
        def backtrack(r,c,i):

            if i==len(word):
                print(path)
                return True
                
            if r<0 or c<0 or r>=R or c>=C or (r,c) in path or word[i]!=board[r][c]:
                return False

            path.add((r,c))
            res = (backtrack(r-1,c,i+1) or backtrack(r,c-1,i+1) or backtrack(r,c+1,i+1) or backtrack(r+1,c,i+1))
            path.remove((r,c))

            return res

        for i in range(R):
            for j in range(C):
                if backtrack(i,j,0): return True
        return False

        