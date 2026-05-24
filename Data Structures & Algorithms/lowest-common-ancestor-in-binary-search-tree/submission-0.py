# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def is_exist(root, node):
            if not root:
                return False
        
            if root.val == node.val:
                return True
            
            return is_exist(root.left, node) or is_exist(root.right, node)
        
        if root.val == p.val or root.val == q.val:
            return root
        
        ps = is_exist(root.left, p)
        qs = is_exist(root.left, q)

        if ps and qs:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if not ps and not qs:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
        