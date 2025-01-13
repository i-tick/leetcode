class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        pre = 0
        for i in range(len(self.nums)):
            pre+=self.nums[i]
            self.nums[i] = pre
        print(self.nums)



    def sumRange(self, left: int, right: int) -> int:
        if left ==0 :
            return self.nums[right]
        else:
            return self.nums[right] - self.nums[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)