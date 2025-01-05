class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")]*n
        prices[src] = 0
        for _ in range(k+1):
            print(prices)
            temp = prices.copy()

            for s,d,cost in flights:
                if prices[s]==float("inf"):
                    continue
                if temp[d]>prices[s]+cost:
                    temp[d] = prices[s]+cost
            prices = temp
        return -1 if prices[dst]== float("inf") else prices[dst]