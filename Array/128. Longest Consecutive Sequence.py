class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        for i in c.keys():
            if i-1 in c.keys():
                continue
            temp=1
            for j in range(1,len(nums)+1):
                if i+j in c.keys():
                    temp+=1
                else:
                    break
            res = max(res,temp)
        return res 
