class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        n = math.floor(len(nums)/3)
        res = []
        for i in c.keys():
            if n<c[i]:
                res.append(i)
        return res
        