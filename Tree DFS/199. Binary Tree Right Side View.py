# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append(root)
        res =[]

        while q:
            qlen = len(q)

            level = []

            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level[-1])
        return res
    # # Alternative approach using BFS with None markers
    # time complexity: O(n)
    # space complexity: O(n)
    





        # if not root:
        #     return []

        # q = deque()
        # q.append(root)
        # q.append(None)
        # res =[]

        # while q:
        #     node = q.popleft()
        #     if node:
        #         res.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     else:
        #         if len(q)==0:
        #             res.append(None)
        #             break
        #         q.append(None)
        #         res.append(None)

        # levels = []
        # for i in range(len(res)):
        #     if res[i]==None:
        #         levels.append(res[i-1])
        # return levels         




        