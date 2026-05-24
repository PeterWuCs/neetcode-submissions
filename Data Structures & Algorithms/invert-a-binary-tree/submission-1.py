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
        
        queeu = [root]

        while queeu:
            node = queeu.pop(0)
            if node.right:
                queeu.append(node.right)
            if node.left:
                queeu.append(node.left)
            node.right, node.left = node.left, node.right
        
        return root

        