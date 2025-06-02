from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by start time, and by end time in descending order for equal start times
        intervals.sort(key = lambda x: (x[0], -x[1]))
        count = 0
        prev_end = float("-inf")
    
        for start, end in intervals:
            if end > prev_end:
                count += 1
                prev_end = end 
                
        return count
# Time Complexity: O(n log n) due to sorting the intervals
# Space Complexity: O(1) for the count and prev_end variables
# Note: The function counts the number of intervals that are not covered by any other interval.
#       An interval [a, b] is covered by another interval [c, d] if c <= a and b <= d.
#       The sorting ensures that we can efficiently check for coverage by comparing the end times.