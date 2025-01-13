class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(len(days)+1)
        cost_map = {1:costs[0], 7:costs[1], 30:costs[2]}
        
        for i in range(len(days)-1,-1,-1):
            j = i
            dp[i] = float('inf')
            for c in cost_map:
                while j<len(days) and days[j] < days[i]+c:
                    j+=1
                dp[i] = min(dp[i], cost_map[c] + dp[j])
        return dp[0]
