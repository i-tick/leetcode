class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        for i in c:
            if c[i]>=3:
                if c[i]%2==0:
                    c[i]=2
                else:
                    c[i]=1
        count= 0
        for i in c:
            count+=c[i]
        return count