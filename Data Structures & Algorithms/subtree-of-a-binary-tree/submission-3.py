# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False

            if (s.val == t.val):
                return isSame(s.right, t.right) and isSame(s.left, t.left)

            return False



        def dfs(root, sub):
            if not sub:
                return True
            if not root:
                return False

            if isSame(root, sub):
                return True
            
            return dfs(root.right, sub) or dfs(root.left, sub)
                


        return dfs(root, subRoot)