class ListNode:
    def __init__(self,val=0,prev=None,nex=None):
        self.val = val
        self.prev=prev
        self.nex=nex
class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.left=ListNode()
        self.right = ListNode()
        self.right.prev=self.left
        self.left.nex = self.right

        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = ListNode(value)
        self.right.prev.nex = new_node
        self.right.prev = new_node
        new_node.prev = self.right.prev
        new_node.nex = self.right
        self.k-=1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.nex.nex.prev=self.left
        self.left.nex=self.left.nex.nex
        self.k+=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.nex.val
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.nex==self.right

    def isFull(self) -> bool:
        return self.k==0

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()