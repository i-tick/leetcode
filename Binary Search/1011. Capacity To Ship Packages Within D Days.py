class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r = sum(weights)
        l = max(weights)
        res = float('inf')
        while l<=r:
            m = (l+r)//2
            d = 0
            s = 0
            for i in weights:
                s+=i
                if s>m:
                    s = i
                    d+=1
                elif s==m:
                    s = 0
                    d+=1

            if s!=0: d+=1
            if d>days:
                l = m+1
            else:
                res = min(res,m)
                r = m-1

        return res

