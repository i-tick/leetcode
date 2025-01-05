class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = Counter(nums)
        res = 0
        for i in l:
            length = 0
            if i-1 not in l:
                length =1
                while (i+length) in l:
                    length+=1
                res = max(res,length)
        return res