class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        i = 0
        for c in s:
            while i<len(t):
                if t[i]!=c:
                    i+=1
                    continue
                else:
                    break
            i+=1
        if i<=len(t):
            return True
        return False