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

            left_to = check(node.left)
            right_to = check(node.right)

            bigges = max(left_to + right_to + node.val, bigges)
            
            if left_to > 0 or right_to > 0:
                if max(left_to, right_to) + node.val > 0:
                    return max(left_to, right_to) + node.val
                else:
                    return 0
            if node.val > 0:
                return node.val
            return 0

        check(root)

        return bigges


