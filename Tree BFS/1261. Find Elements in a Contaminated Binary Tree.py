# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.elem = set()
        if not root:
            return 
        root.val = 0
        q = deque([root])
        self.elem.add(0)
        while q:
            qlen = len(q)
            for _ in range(qlen):
                node = q.popleft()
                if node.left:
                    node.left.val = (2*node.val) + 1
                    self.elem.add(node.left.val)
                    q.append(node.left)
                if node.right:
                    node.right.val = (2*node.val) + 2
                    self.elem.add(node.right.val)
                    q.append(node.right)
        return
        

    def find(self, target: int) -> bool:
        if target in self.elem:
            return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)