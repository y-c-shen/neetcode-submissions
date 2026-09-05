# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getMaxDepth(node):
            left_depth, right_depth = 0, 0
            if not node: return 0
            if not node.right and not node.left:
                return 1
            if node.right:
                right_depth = 1 + getMaxDepth(node.right)
            if node.left:
                left_depth = 1 + getMaxDepth(node.left)
            return max(left_depth, right_depth)
        return getMaxDepth(root)
            