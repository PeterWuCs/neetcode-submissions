# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(p, q):
            
            if not p and q:
                return False
            if not q and p:
                return False
            if not p and not q:
                return True
            if p.val != q.val:
                return False


            
            return helper(p.right, q.right) and helper(p.left, q.left)

        
        return helper(p, q)


            