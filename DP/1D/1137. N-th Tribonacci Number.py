class Solution:
    def tribonacci(self, n: int) -> int:
        f = 0
        s = 1
        t = 1
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        for i in range(3,n+1):
            temp = f + s + t
            f = s
            s = t
            t = temp
        return t
        