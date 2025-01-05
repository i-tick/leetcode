class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if target == nums[mid]:
                return mid


            # check for left portion 
            if nums[l]<=nums[mid]:
                # check to go which side
                if target>nums[mid]: # go right
                    l = mid+1
                elif target<nums[l]: # got right
                    l = mid+1
                else: # go left
                    r = mid-1
            else:
                if target<nums[mid]:
                    r = mid-1
                elif nums[r]<target:
                    r = mid - 1
                else:
                    l = mid+1
        return -1
            
