class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = Counter(nums)
        d = [[] for i in range(len(nums)+1)]
        for i in l:
            d[l[i]].append(i)

        res = []

        for i in range(len(d)-1,0,-1):
            for j in d[i]:
                res.append(j)
                if len(res) == k:
                    return res
        