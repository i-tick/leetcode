class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = n
        res = 0
        while l<=r:
            mid = (l+r)//2
            coins = (mid) * (mid+1)/2

            if coins > n:
                r = mid-1
            else:
                l = mid+1
                res = max(mid,res)
        return res
        