# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        bigges = float("-inf")

        def check(node):
            nonlocal bigges

            if not node:
                return 0

            left_to = max(check(node.left), 0)
            right_to = max(check(node.right), 0)

            bigges = max(bigges, node.val + left_to + right_to)

            return max(left_to, right_to) + node.val
           
        check(root)
        return bigges


