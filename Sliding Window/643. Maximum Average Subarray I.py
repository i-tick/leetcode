class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = dict(Counter(nums))
        l = list(counter.keys())
        l.sort()
        print(l)
        res = 0
        for i in range(1,len(l)):
            if abs(l[i] - l[i-1]) ==1:
                res = max(res,counter[l[i]]+counter[l[i-1]])
        return res

        