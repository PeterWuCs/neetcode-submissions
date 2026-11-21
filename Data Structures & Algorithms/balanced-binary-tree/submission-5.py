# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return True, 0

            if not node.right and node.left:
                if node.left.left or node.left.right:
                    return False, 0
            
            if not node.right and node.left:
                if node.left.left and node.left.right:
                    return False, 0


            left, left_height = dfs(node.left)
            right, right_height = dfs(node.right)

            if not left or not right:
                return False, 0


            if abs(left_height - right_height) > 1:
                return False, 0

            return True, max(left_height, right_height) + 1



        ans,_ = dfs(root)

        return ans