class MyQueue:

    def __init__(self):
        self.s = []
        

    def push(self, x: int) -> None:
        self.s.append(x)
        

    def pop(self) -> int:
        t = self.s[0]
        del self.s[0]
        return t
        

    def peek(self) -> int:
        return self.s[0]

        

    def empty(self) -> bool:
        print(self.s)
        return len(self.s)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()