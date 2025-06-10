from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        mat = [[0]*col for _ in range(row)]
        day = 0
        dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1, 0), (1,1)]
        water_cells = [(r-1,c-1) for r,c in cells]

        # Create virtual nodes for left and right sides
        left_node = 0
        right_node = row*col + 1

        # Initialize parent array for union-find
        par = [i for i in range(row*col + 2)]
        def find(n):
            if n!=par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            par1 = find(n1)
            par2 = find(n2)
            par[max(par1,par2)] = min(par1,par2)


        for r,c in water_cells:
            mat[r][c] = 1
            # Union the current cell with its neighbors
            for dr,dc in dirs:
                if 0<=r+dr<row and 0<=c+dc<col and mat[r+dr][c+dc] == 1:
                    union(r*col + c, ((r+dr)*col) + (c+dc))
            # If the current cell is in the first column, union it with the left node
            if c==0:
                union(r*col+c, left_node)
            # If the current cell is in the last column, union it with the right node
            if c==col-1:
                union(r*col+c,right_node)

        # Check if there is a path from the left node to the right node
            if find(left_node)==find(right_node):
                return day
            day += 1
        return day 

        