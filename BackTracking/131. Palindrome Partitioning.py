class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        substring = []

        def backtrack(i):
            if i==len(s):
                res.append(substring.copy())
                return

            for j in range(i,len(s)):
                if ispalin(s,i,j):
                    substring.append(s[i:j+1])
                    backtrack(j+1)
                    substring.pop()

        def ispalin(s,l,r):
            return s[l:r+1] == s[l:r+1][::-1]
        
        backtrack(0)
        return res
