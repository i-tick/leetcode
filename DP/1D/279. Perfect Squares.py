class Solution:
    def numSquares(self, n: int) -> int:
        r = math.floor(math.sqrt(n))
        arr = [i*i for i in range(r+1)]
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for a in range(n+1):
            for c in arr:
                if a-c>=0:
                    dp[a] = min(dp[a],1+dp[a-c])
        return dp[n] if dp[n]!=float('inf') else -1

        