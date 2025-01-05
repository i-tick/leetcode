class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.k = k
        for i in nums:
            if len(self.minheap)>=k:
                heapq.heappushpop(self.minheap,i)
            else:
                heapq.heappush(self.minheap,i)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap,val)
        if len(self.minheap)>self.k:
            heapq.heappop(self.minheap)

        res = heapq.heappop(self.minheap)
        heapq.heappush(self.minheap,res)
        return res

        


# # Your KthLargest object will be instantiated and called as such:
# # obj = KthLargest(k, nums)
# # param_1 = obj.add(val)
