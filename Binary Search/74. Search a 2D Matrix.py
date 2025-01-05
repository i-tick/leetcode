class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])


        def binary(nums,target):
            l = 0
            r = len(nums) - 1

            while l<=r:
                mid = (l+r)//2
                if nums[mid] > target:
                    r = r-1
                elif nums[mid] < target:
                    l = l+1
                else:
                    return True
            return False
        for i in range(rows):
            if target >= matrix[i][0] and target <= matrix[i][cols-1]:
                return binary(matrix[i],target)
        return False

        