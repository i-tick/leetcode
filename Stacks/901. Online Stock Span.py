class StockSpanner:

    def __init__(self):
        self.arr = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.arr and self.arr[-1][0]<=price:
            span+=self.arr[-1][1]
            self.arr.pop()
        self.arr.append([price,span])
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)