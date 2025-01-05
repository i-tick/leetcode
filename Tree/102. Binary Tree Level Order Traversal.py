# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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


        