class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        while i<n and intervals[i][0] < newInterval[0]:
            result.append(intervals[i])
            i+=1
        if not result or result[-1][1]<newInterval[0]:
            result.append(newInterval)
        else:
            result[-1][1] = max(result[-1][1], newInterval[1])
        
        while i<n:
            u = intervals[i][0]
            v = intervals[i][1]
            if result[-1][1] < u:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], v)
            i+=1
        return result 
# Time Complexity: O(n) where n is the number of intervals
# Space Complexity: O(n) for the result list
# Note: The input intervals are assumed to be non-overlapping and sorted by their start times.
#       The new interval is also assumed to be non-overlapping with the existing intervals.
#       The function merges the new interval into the existing intervals while maintaining the sorted order.