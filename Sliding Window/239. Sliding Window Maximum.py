class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        q = deque()
        l = 0
        r = 0
        n = len(nums)
        for r in range(n):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            if l>q[0]:
                q.popleft()
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
        return output
