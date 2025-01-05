# O(N*M)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        num2Idx = {n:i for i,n in enumerate(nums2)}

        for i,n in enumerate(nums1):
            idx = num1Idx[n]
            for j in range(idx,len(nums2)):
                if nums2[j]>n:
                    res[i] = nums2[j]
                    break
        return res



# O(N+M)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        num1Idx = {n:i for i,n in enumerate(nums1)}

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and stack[-1]<cur:
                x = stack.pop()     
                idx = num1Idx[x]
                res[idx] = cur
            if cur in num1Idx:
                stack.append(cur)
        return res