from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def cleanup(r, q, nums):
            while q and nums[q[-1]]<=nums[r]:
                q.pop()
        output = []
        q = deque()
        l = 0
        r = 0
        n = len(nums)
        for r in range(n):
            cleanup(r, q, nums)
            q.append(r)
            if q and l>q[0]:
                q.popleft()
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
        return output
#         # time complexity: o(n)
#         # space complexity: o(k) for the deque