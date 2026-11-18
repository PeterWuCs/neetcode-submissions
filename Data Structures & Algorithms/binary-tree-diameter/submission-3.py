# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def helper(root):
            if not root:
                return 
            
            if not root.left and not root.right:
                return 0
            left_path = 0
            right_path = 0
            
            if root.left:
                left_path = 1 + helper(root.left)
            if root.right:
                right_path = 1 + helper(root.right)

            res[0] = max(res[0], left_path + right_path)

            return max(left_path, right_path)
        helper(root)
        return res[0]