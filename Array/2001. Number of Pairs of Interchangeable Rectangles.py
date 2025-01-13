class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        d = {}
        for a,b in rectangles:
            if a/b in d:
                d[a/b][1] = d[a/b][1] + d[a/b][0]
                d[a/b][0] += 1
            else:
                d[a/b] = [1,0]
        res = 0
        for i in d:
            res+=d[i][1]
        return res
        