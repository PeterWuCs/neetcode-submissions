# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [ ]

        curr = root
        while curr:
            stack.append(curr)
            curr = curr.left

        while stack:
            node = stack.pop(-1)
            if k == 1:
                return node.val
            else:
                k -= 1

            if node.right:
                curr = node.right
                while curr:
                    stack.append(curr)
                    curr = curr.left

        return -1

