class Solution:
    def search(self, nums: List[int], target: int) -> bool:


        l = 0
        n = len(nums)
        r = n-1

        while l<=r:
            print(l,r)
            m = (l+r)//2

            if nums[m]==target:
                return True
            if nums[l]==nums[m]:
                l+=1
                continue
            if nums[r]==nums[m]:
                r-=1
                continue

            if nums[l]<=nums[m]:
                if target>=nums[l] and target<nums[m]:
                    r-=1
                else:
                    l+=1
            else:
                if target<=nums[r] and target>nums[m]:
                    l+=1
                else:
                    r-=1
        return False

        