class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i,subset,sum):        
            if sum==target:
                res.append(subset.copy())
                return
            if i>=len(nums) or sum>target:
                return 

            subset.append(nums[i])
            dfs(i+1,subset,sum+nums[i])
            subset.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,subset,sum)

        dfs(0,[],0)
        return res
        
        