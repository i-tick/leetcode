class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        n = len(nums)
        vis = set()
        for i in range(n):
            t = nums[i]
            while i not in vis:
                new_idx = (i+k)%n
                new_t = nums[new_idx]
                nums[new_idx] = t
                t = new_t
                vis.add(i)
                i = new_idx
        return nums


        