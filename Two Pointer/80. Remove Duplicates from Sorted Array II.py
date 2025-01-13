class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1,len(nums)):
            if i<len(nums)-1 and nums[i]==nums[i-1] and nums[i]==nums[i+1]:
                pass
            else:
                nums[k]=nums[i]
                k+=1
        return k
        
        