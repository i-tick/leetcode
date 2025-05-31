from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sub_array_sum = sum(nums[:k])
        avg = sub_array_sum/k
        for i in range(k,len(nums)):
            sub_array_sum += nums[i]-nums[i-k]
            avg = max(avg, sub_array_sum/k)
        return avg
    # Time Complexity: O(n)
    # Space Complexity: O(1)


        