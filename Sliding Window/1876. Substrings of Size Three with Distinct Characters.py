class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        l = 0
        r = 3
        c = 0
        counter = dict(Counter(s[:r]))
        while r<=len(s):            
            if len(counter)==3:
                c+=1
            counter[s[l]]-=1
            if counter[s[l]]==0:
                del counter[s[l]]
            if r<len(s):
                counter[s[r]] = 1+counter.get(s[r],0)
            l+=1
            r+=1
        return c
            
            
            
        