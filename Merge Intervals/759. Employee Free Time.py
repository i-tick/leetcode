
# We are given a list schedule of employees, which represents the working time for each employee.

# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

# (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. 
# For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include 
# intervals like [5, 5] in our answer, as they have zero length.

 

# Example 1:

# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation: There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
# Example 2:

# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]



# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

import heapq

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]': # type: ignore
        schedules = []

        for intervals in schedule:
            [schedules.append(x) for x in intervals]

        schedules.sort(key=lambda x: x.start)
        res = []
        last_max_end_time = schedules[0].end

        for interval in schedules:
            # there is overlap
            if interval.start <= last_max_end_time:
                last_max_end_time = max(last_max_end_time, interval.end)
                continue
            # no overlap
            if interval.start > last_max_end_time:
                res.append(Interval(last_max_end_time, interval.start))
                last_max_end_time = interval.end

        return res
# Time Complexity: O(N log N) where N is the total number of intervals across all employees.
# Space Complexity: O(N) for the schedules list, where N is the total number of intervals across all employees.
# Note: The function finds the free time intervals when no employee is working, based on their schedules.



    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]': # type: ignore
        heap_arr = []
        for i in range(len(schedule)):
            heap_arr.append((schedule[i][0].start, i , 0))

        heapq.heapify(heap_arr)
        res = []
        previous = schedule[heap_arr[0][1]][heap_arr[0][2]].end

        while heap_arr:
            _, i, j = heapq.heappop(heap_arr)

            interval = schedule[i][j]

            if interval.start > previous:
                res.append(Interval(previous, interval.start))

            previous = max(previous, interval.end)

            if j+1<len(schedule[i]):
                heapq.heappush(heap_arr, (schedule[i][j+1].start, i, j+1))

        return res
# Time Complexity: O(N log K) where N is the total number of intervals across all employees and K is the number of employees.
# Space Complexity: O(K) for the heap, where K is the number of employees.
# Note: The function finds the free time intervals when no employee is working, based on their schedules.