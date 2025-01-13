class Solution:
    def minSwaps(self, s: str) -> int:
        o = 0
        c = 0

        for i in s:
            if i=='[':
                o+=1
            if i==']':
                if o<=0:
                    c+=1
                    o+=1
                else:
                    o-=1
        return c