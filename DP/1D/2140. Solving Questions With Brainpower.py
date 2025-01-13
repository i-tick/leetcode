class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            
            if i>=len(questions):
                return 0
            dp[i] = max(dfs(i+1), questions[i][0]+dfs(i+1+questions[i][1]))
            return dp[i]

        dfs(0)
        return dp[0]