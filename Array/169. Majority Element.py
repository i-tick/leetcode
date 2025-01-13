# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        maxc = 0
        res = -1
        for n in nums:
            if n in hash:
                hash[n] = 1+hash[n]
            else:
                hash[n] = 0
            res = n if hash[n]>maxc else res
            maxc = max(hash[n],maxc)
        return res
    


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i in c:
            if c[i]>math.floor(len(nums)/2):
                return i