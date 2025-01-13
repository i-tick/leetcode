class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+2)
        dp[len(s)+1] = 0
        dp[len(s)] = 1

        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                dp[i] = 0
                continue
            if (i+1)<len(s) and ((s[i] in '1' and s[i+1] in '0123456789') or (s[i] in '2' and s[i+1] in '0123456')):
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        return dp[0]
        