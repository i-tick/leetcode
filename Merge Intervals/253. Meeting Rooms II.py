import heapq
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        min_heap = []

        for u,v in intervals:
            if min_heap and min_heap[0]<=u:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, v)
        return len(min_heap)