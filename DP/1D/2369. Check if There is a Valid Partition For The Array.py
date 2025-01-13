class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False]*(len(nums)+1)
        dp[len(nums)]=True

        for i in range(len(nums)-1,-1,-1):
            if i+3<=len(nums) and nums[i]==nums[i+1] and nums[i]==nums[i+2] and not dp[i]:
                dp[i] = dp[i+3]
            if i+3<=len(nums) and nums[i]+1==nums[i+1] and nums[i+1]+1==nums[i+2] and not dp[i]:
                dp[i] = dp[i+3]
            if i+2<=len(nums) and nums[i]==nums[i+1] and not dp[i]:
                dp[i] = dp[i+2]
            # print(dp)
        return dp[0]
        
        