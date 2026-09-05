# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def getHeight(node):
            if not node:
                return 0
            height_left = getHeight(node.left)
            height_right = getHeight(node.right)
            nonlocal max_diameter
            max_diameter = max(max_diameter, height_left + height_right)
            return 1 + max(getHeight(node.left), getHeight(node.right))

        if not root:
            return 0
        getHeight(root)
        return max_diameter
        
        
                
        