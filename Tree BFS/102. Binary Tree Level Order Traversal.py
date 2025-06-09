# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                res.append(level)
        return res
        # Time complexity: O(n)
        # Space complexity: O(n) for the queue and the result list
        # Note: This implementation uses a queue to perform a level order traversal of the binary tree.
        # It processes each level of the tree, collecting the values of nodes at that level into a list,
        # which is then appended to the result list. The queue allows for efficient processing of nodes in a breadth-first manner.
        # The while loop continues until there are no more nodes to process in the queue.

# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

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
        # temp = []
        # levels = []
        # for i in res:
        #     if i!=None:
        #         temp.append(i)
        #     else:
        #         levels.append(temp)
        #         temp=[]

        # return levels         




        # res = [[root.val]]
        # l = [[root]]
        # c = 0
        # while len(l[c]):
        #     temp = []
        #     temp1 = []
        #     for i in l[c]:
        #         if i.left:
        #             temp.append(i.left)
        #             temp1.append(i.left.val)
        #         if i.right:
        #             temp.append(i.right)
        #             temp1.append(i.right.val)

        #     if temp!=[]:
        #         c+=1
        #         l.append(temp)
        #         res.append(temp1)
        #     else:
        #         break
        # return res


        