from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0

        while i<len(firstList) and j<len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start<=end:
                result.append([start, end])

            if firstList[i][1] < secondList[j][1]:
                i+=1
            else:
                j+=1

        return result
# Time Complexity: O(n + m) where n and m are the lengths of the two lists
# Space Complexity: O(1) for the result list, which can be at most min(n, m) in size
# Note: The input lists are assumed to be non-overlapping and sorted by their start times.
#       The function finds the intersection of the two lists of intervals and returns a new list of intervals that represent the intersections.