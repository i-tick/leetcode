# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 0 , 0)) # node, col, row
        res = defaultdict(list)
        min_column = float("inf")
        max_column = float("-inf")
        while q:
            qlen = len(q)
            for i in range(qlen):
                node, col, row = q.popleft()
                min_column = min(min_column, col)
                max_column = max(max_column, col)
                res[col].append(node.val)
                if node.left:
                    q.append((node.left, col - 1, row + 1))
                if node.right:
                    q.append((node.right, col + 1, row + 1))
        res_list = []
        for i in range(min_column, max_column+1):
            res_list.append(res[i])
        return res_list