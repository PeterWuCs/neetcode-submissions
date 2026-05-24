# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def check(root, max):
            if not root:
                return 0
            if max <= root.val:
                return 1 + check(root.right, root.val) + check(root.left, root.val)

            return check(root.right, max) + check(root.left, max)

        if not root:
            return 0

        return 1 + check(root.right, root.val) + check(root.left, root.val)