# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        q = [root]
        s = []

        depth = 0

        while q:
            node = q.pop()
            
            if not node:
                continue
            
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
            
            if not q:
                depth += 1
                s, q = q, s
        
        return depth
