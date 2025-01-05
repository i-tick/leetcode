class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for i in nums:
            if len(minheap)>=k:
                heapq.heappushpop(minheap,i)
            else:
                heapq.heappush(minheap,i)
        return minheap[0]
        