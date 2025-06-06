from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
  
        r_largest_min = float('-inf')
        for i in range(M):
            r_min = min(matrix[i])  
            r_largest_min = max(r_largest_min, r_min)
    
        c_smallest_max = float('inf')
        for i in range(N):
            c_max = max(matrix[j][i] for j in range(M))
            c_smallest_max = min(c_smallest_max, c_max)
    
        if r_largest_min == c_smallest_max:
            return [r_largest_min]
        else:
            return []