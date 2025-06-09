# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        res =[]

        while q:
            qlen = len(q)
            level = []
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        flag = 1
        levels = []
        for i in res:
            levels.append(i[::flag])
            flag = flag*-1

        return levels   
    # Time complexity: O(n)
    # Space complexity: O(n)
    # We use a queue to perform level order traversal of the binary tree.
    # For each level, we collect the values of nodes into a list.
    # After collecting all levels, we reverse the order of values in every second level.
    # This is done by using a flag that alternates between 1 and -1, which determines the slicing direction.
    # The final result is a list of lists, where each inner list represents a level of the tree with zigzag ordering.