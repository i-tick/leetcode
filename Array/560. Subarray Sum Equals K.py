class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixdict = defaultdict(int)
        pfix = 0
        res = 0
        prefixdict[0]=1
        for i in range(len(nums)):
            pfix +=nums[i]
            if pfix-k in prefixdict:
                res+=prefixdict[pfix-k]
            prefixdict[pfix]+=1
            
        return res
        