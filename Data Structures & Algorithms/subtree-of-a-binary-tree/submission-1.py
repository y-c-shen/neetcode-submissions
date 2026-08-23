# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check_subtree(root, subtree):
            if root and not subtree: return False
            if not root and subtree: return False
            if not root and not subtree: return True
            else: 
                if root.val == subtree.val:
                    return check_subtree(root.right, subtree.right) and check_subtree(root.left, subtree.left)
                else: return False

        if not root and not subRoot: return True
        if root and not subRoot: return False
        if not root and subRoot: return False
        if root.val == subRoot.val:
            # check if its a valid subtree
            if check_subtree(root, subRoot): return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)