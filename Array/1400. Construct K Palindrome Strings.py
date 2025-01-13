class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        res = 0
        c = Counter(s)
        for char in c:
            if c[char]%2!=0:
                res+=1
        if res==k:
            return True
        if res<k and len(s)>=k:
            return True
        return False
        