from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x: x[0])

        occupied = 0
        start = meetings[0][0]
        end = meetings[0][1]
        for u,v in meetings:
            if u<=end:
                end  = max(end,v)
            else:
                occupied += end-start+1
                start = u
                end = v
        occupied+=end-start+1
        
        return days-occupied      
# Time Complexity: O(n log n) due to sorting the meetings
# Space Complexity: O(1) for the occupied variable
# Note: The function counts the number of days without meetings by calculating the total occupied days based on the given meeting intervals.