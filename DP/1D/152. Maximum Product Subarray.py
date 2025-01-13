class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        front = []
        last = []
        cur = 1
        if (len(nums)==1):
            return nums[0]
        for i in range(len(nums)):
            if nums[i]!=0:
                cur = cur*nums[i]
                front.append(max(nums[i],cur))

            else:
                cur = 1
                front.append(0)
        cur=1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]!=0:
                cur = cur*nums[i]
                last.append(max(nums[i],cur))
            else:
                cur=1
                last.append(0)
        return max(max(front),max(last))