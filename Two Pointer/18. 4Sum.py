class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        def call(nums,target,val):
            for i in range(len(nums)):
                l = 0
                r = len(nums)-1
                while (l<i and i<r):
                    if (nums[l]+nums[i]+nums[r])>target:
                        r-=1
                    elif (nums[l]+nums[i]+nums[r])<target:
                        l+=1
                    else:
                        if [val,nums[l],nums[i],nums[r]] not in ans:
                            ans.append([val,nums[l],nums[i],nums[r]])
                        r-=1
                        l+=1
        for i in range(n-1):
            call(nums[i+1:],target-nums[i],nums[i])
        return ans
        