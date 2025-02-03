# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        q.append(None)
        res =[]

        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                if len(q)==0:
                    res.append(None)
                    break
                q.append(None)
                res.append(None)
        temp = []
        levels = []
        flag = -1
        for i in res:
            if i!=None:
                temp.append(i)
            else:
                flag*=-1
                if flag ==1:
                    levels.append(temp)
                else:
                    levels.append(temp[::-1])
                temp=[]

        return levels         
