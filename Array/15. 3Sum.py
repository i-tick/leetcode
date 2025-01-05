class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            l = 0
            r = len(nums)-1
            while (l<i and i<r):
                if (nums[l]+nums[i]+nums[r])>0:
                    r-=1
                elif (nums[l]+nums[i]+nums[r])<0:
                    l+=1
                else:
                    if [nums[l],nums[i],nums[r]] not in ans:
                        ans.append([nums[l],nums[i],nums[r]])
                    r-=1
                    l+=1
        return ans