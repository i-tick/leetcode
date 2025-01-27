
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = {}
        for i in t:
            if i not in c:
                c[i] = 1
            else:
                c[i] +=1
        l = 0
        r = 0
        need = len(c)
        have = 0
        res = ''
        fin_r = -1
        fin_l = -1
        min_s = float('inf')
        hash = {}
        for r in range(len(s)):
            if s[r] in hash:
                hash[s[r]]+=1
            else:
                hash[s[r]] = 1
            if s[r] in c and hash[s[r]] == c[s[r]]:
                have +=1
            
            while have==need:
                min_s = min(min_s, r-l+1)
                if min_s == r-l+1:
                    fin_r = r
                    fin_l = l
                if hash[s[l]]>=1:
                    hash[s[l]]-=1
                if s[l] in c and hash[s[l]]<c[s[l]]:
                    have-=1
                l+=1
        return s[fin_l:fin_r+1]