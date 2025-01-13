class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R = len(matrix)
        C = len(matrix[0])
        self.sumMatrix = []
        for r in range(R+1):
            row = [0]*(C+1)
            self.sumMatrix.append(row)


        for r in range(R):
            pre = 0
            for c in range(C):
                pre+=matrix[r][c]
                above = self.sumMatrix[r][c+1]
                self.sumMatrix[r+1][c+1] = pre+above

        


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 = row1+1
        c1 = col1+1

        r2 = row2+1
        c2 = col2+1

        current_sum = self.sumMatrix[r2][c2]
        left_sum = self.sumMatrix[r2][c1-1]
        top_sum = self.sumMatrix[r1-1][c2]
        topleft_sum = self.sumMatrix[r1-1][c1-1]

        return current_sum - left_sum - top_sum + topleft_sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)