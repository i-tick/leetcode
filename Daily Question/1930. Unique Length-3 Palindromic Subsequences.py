class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        counter = Counter(s)
        right = counter
        right[s[0]] -=1
        left = defaultdict(int)
        left[s[0]] = 1
        res = set() # (mid,out)
        count = 0
        for m in range(1,len(s)-1):
            right[s[m]]-=1
            for i in range(26):
                c = chr(ord('a')+i)
                if c in left and left[c]>=1 and c in right and right[c]>=1:
                    if (s[m],c) not in res:
                        res.add((s[m],c))
                        count+=1
            left[s[m]] +=1
        return count
            

        