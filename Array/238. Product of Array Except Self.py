class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # Time O(n) 
        # # space O(n)
        # count_z = 0
        # product = 1
        # for i in nums:
        #     if i==0:
        #         count_z +=1
        #     else:
        #         product*=i
        
        # if count_z>1:
        #     return [0]*len(nums)

        # output = []
        # for i in nums:
        #     if i==0:
        #         output.append(product)
        #     else:
        #         if count_z == 1:
        #             output.append(0)
        #         else: 
        #             output.append(product//i)
        # return output



        # Time O(n) 
        # space O(1)
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res