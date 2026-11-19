# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        largest = float('-inf')

        
        def dfs(root):
            nonlocal largest

            left_sum = 0
            right_sum = 0

            if root.left:
                left_sum = dfs(root.left)

            if root.right:
                right_sum = dfs(root.right)

            cur_max = max(root.val, root.val + left_sum, root.val + right_sum)

            largest = max(largest, cur_max, root.val + left_sum + right_sum)

            return cur_max

        largest = max(dfs(root), largest)

        return largest