# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        start = 0
        end = len(nums)
        mid = (start+end)//2
        if end==0:
            return None
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[start:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
        