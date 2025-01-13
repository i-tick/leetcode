class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = -1
        for k in c.keys():
            if k-1 not in c.keys():
                if k-2 in c.keys():
                    res =  k-1
                    if res>0:
                        break
                else:
                    res =  k+len(nums)
                    if res>0:
                        break
            else:
                continue

        for i in range(1,res+len(nums)):
            if i not in c:
                return i
        return 1
        