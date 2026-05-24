# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = None
        right = None
        if root.right:
            left = self.invertTree(root.right)
        
        if root.left:
            right = self.invertTree(root.left)
        
        root.right = right
        root.left = left
        return root
        