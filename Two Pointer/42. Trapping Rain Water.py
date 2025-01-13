class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        minlr = [float('inf')]*n
        maxl,maxr = float('-inf'), float('-inf')

        for i in range(len(height)):
            maxl = max(maxl,height[i])
            minlr[i] = min(minlr[i],maxl)

        for i in range(len(height)-1,-1,-1):
            maxr = max(maxr,height[i])
            minlr[i] = min(minlr[i],maxr)

        s = 0
        for i in range(len(height)):
            if (minlr[i]-height[i]) > 0:
                s+=minlr[i]-height[i]
        return s