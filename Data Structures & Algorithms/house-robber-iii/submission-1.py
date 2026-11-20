# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def helper(root):
            if not root:
                return 0

            if root in memo:
                return memo[root]

            right_with_cur = 0
            right_without_cur = 0

            if root.right:
                right_without_cur = helper(root.right)
                right_with_cur = helper(root.right.right) + helper(root.right.left)
            
            left_with_cur = 0
            left_without_cur = 0

            if root.left:
                left_without_cur = helper(root.left)
                left_with_cur = helper(root.left.right) + helper(root.left.left)
            
            memo[root] = max(right_with_cur + left_with_cur + root.val, right_without_cur + left_without_cur)

            return memo[root]

        helper(root)
        return memo[root]