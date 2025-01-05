class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perms, nums, checker):
            if len(nums) == len(perms):
                res.append(perms.copy())
                return

            for i in range(len(nums)):
                if not checker[i]:
                    perms.append(nums[i])
                    checker[i] = True
                    backtrack(perms,nums,checker)
                    perms.pop()
                    checker[i] = False

        backtrack([],nums,[False] * len(nums))
        return res
        