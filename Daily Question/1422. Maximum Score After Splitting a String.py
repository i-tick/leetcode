class Solution:
    def maxScore(self, s: str) -> int:
        counter = Counter(s)
        r = counter['1']
        

        l = 0
        max_score = float('-inf')
        for i in range(len(s)-1):
            if s[i]=='0':
                l+=1
            else:
                r-=1
            max_score = max(l+r, max_score)
        return max_score

        