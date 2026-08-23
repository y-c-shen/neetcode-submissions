# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        s = deque()
        s.append(root)
        res = []
        while s:
            layer = []
            for i in range(len(s)):
                node = s.popleft()
                layer.append(node.val)
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
            res.append(layer)
        return res
