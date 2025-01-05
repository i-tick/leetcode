class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,subset,sum):        
            if sum==target:
                res.append(subset.copy())
                return
            if i>=len(nums) or sum>target:
                return 

            subset.append(nums[i])
            dfs(i,subset,sum+nums[i])
            subset.pop()
            dfs(i+1,subset,sum)

        dfs(0,[],0)
        return res
        