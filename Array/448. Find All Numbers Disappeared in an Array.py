class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n) - 1
            if nums[i]>0:
                nums[i] = -1 * nums[i]


        res = []
        for i,n in enumerate(nums):
            if n>0:
                res.append(i+1)
        return res
        