class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        odd = 0
        res = 0
        for i in counter:
            if counter[i]%2!=0:
                odd+=1
            res+=counter[i]//2
        return (res*2) + 1 if odd!=0 else res*2
        