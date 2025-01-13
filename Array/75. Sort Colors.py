class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        z = 0
        o = 0
        t = n-1

        while o<=t:
            if nums[o] == 0:
                temp = nums[z]
                nums[z] = nums[o]
                nums[o] = temp
                z+=1
                o+=1
            elif nums[o]==1:
                o+=1
            else:
                temp = nums[t]
                nums[t] = nums[o]
                nums[o] = temp
                t-=1
