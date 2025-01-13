class Solution:
    def rob(self, nums: List[int]) -> int:


        def helper(arr):
            if len(arr)<=2:
                return max(arr)
            res = []
            res.append(arr[0])
            res.append(max(arr[0],arr[1]))

            for i in range(2,len(arr)):
                val = max(res[i-2]+arr[i],res[i-1])
                res.append(val)
            return res[len(arr)-1] 
        
        if len(nums)<=2:
                return max(nums)
        return max(helper(nums[1:]),helper(nums[:-1]))
        