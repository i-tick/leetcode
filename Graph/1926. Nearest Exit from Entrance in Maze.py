class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        R = len(maze)
        C = len(maze[0])

        q = deque()
        q.append(entrance)
        dist = 1
        vis = set()
        vis.add((entrance[0],entrance[1]))
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                dirs = [[-1,0],[1,0],[0,-1],[0,1]]
                for dirr,dirc in dirs:
                    row = r+dirr
                    col = c+dirc
                    if (row not in range(R) or col not in range(C) or maze[row][col]=='+' or (row,col) in vis):
                        continue
                    if row==0 or col==0 or row == R-1 or col == C-1:
                        return dist
                    q.append([row,col])
                    vis.add((row,col))
            dist+=1
        return -1

        