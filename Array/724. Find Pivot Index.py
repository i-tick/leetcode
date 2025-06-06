class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        totalSum = sum(nums)

        for i in range(len(nums)):
            rightSum = totalSum - nums[i] - leftSum
            if rightSum == leftSum:
                return i
            leftSum += nums[i]

        return -1
        