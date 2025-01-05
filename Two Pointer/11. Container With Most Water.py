class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        cont = 0

        while l<r:
            cont = max(cont,(r-l)*min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            else:
                r-=1
        return cont
