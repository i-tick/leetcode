class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = sum(nums)
        ls = 0
        rs = 0   
        c = 0

        for i in range(len(nums)-1):
            ls += nums[i]
            rs = s - ls
            if ls>=rs:
                print(i)
                c+=1
        return c

        