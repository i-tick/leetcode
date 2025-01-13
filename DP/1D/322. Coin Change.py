class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount==0:
        #     return 0

        # q = deque()
        # q.append(0)
        # res = 1
        # vis = set()
        # vis.add(0)
        # while q:
        #     for i in range(len(q)):
        #         cur_am = q.popleft()
        #         for c in coins:
        #             if cur_am + c == amount:
        #                 return res
        #             if cur_am + c<amount and cur_am + c not in vis:
        #                 q.append(cur_am + c)
        #                 vis.add(cur_am + c)
        #     res+=1
        # return -1
                

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for a in range(amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a],1+dp[a-c])
        return dp[amount] if dp[amount]!=float('inf') else -1