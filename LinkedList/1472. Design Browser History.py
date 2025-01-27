class Node:
    def __init__(self,val,prev=None,nex=None):
        self.val=val
        self.prev=prev
        self.nex=nex

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur=Node(homepage)

    def visit(self, url: str) -> None:
        self.cur.nex = Node(url,self.cur)
        self.cur=self.cur.nex
        

    def back(self, steps: int) -> str:
        while self.cur.prev and steps>0:
            self.cur = self.cur.prev
            steps-=1
        return self.cur.val
        

    def forward(self, steps: int) -> str:
        while self.cur.nex and steps>0:
            self.cur = self.cur.nex
            steps-=1
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)