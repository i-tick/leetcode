class Solution:
    def rob(self, nums: List[int]) -> int:

        # https://youtu.be/73r3KWiEvyk?si=LzsaMofKgLk3s8jJ

        if len(nums)<=2:
            return max(nums)
        res = []
        res.append(nums[0])
        res.append(max(nums[0],nums[1]))

        for i in range(2,len(nums)):
            val = max(res[i-2]+nums[i],res[i-1])
            res.append(val)
        return res[len(nums)-1] 