from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for u,v in intervals:
            if u<=end:
                end  = max(end,v)
            else:
                res.append([start, end])
                start = u
                end = v
        res.append([start, end])            
        return res
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for the result list