class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i>high:
                return 0
            if i>=low:
                dp[i] = 1
            else:
                dp[i] = 0

            dp[i] += dfs(i+zero)+dfs(i+one)
            return dp[i]%(10**9+7)
        return dfs(0)
        