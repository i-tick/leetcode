class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        res_s = ''
        for i in range(len(s)):
            l=r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if res<r-l+1:
                    res_s = s[l:r+1]
                    res = r-l+1
                r+=1
                l-=1
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if res<r-l+1:
                    res_s = s[l:r+1]
                    res = r-l+1
                r+=1
                l-=1
        return res_s
            