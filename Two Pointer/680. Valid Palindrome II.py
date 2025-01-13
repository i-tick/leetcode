class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l<=r:
            if s[l]!=s[r]:
                skipl = s[:l] + s[l+1:]
                skipr = s[:r] + s[r+1:]
                return (skipl == skipl[::-1]) or (skipr == skipr[::-1])
            l+=1
            r-=1
        return s[:] == s[::-1]
        