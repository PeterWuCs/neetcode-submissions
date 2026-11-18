# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append([cur, True])
                cur = cur.left

            if stack and stack[-1][0].right and stack[-1][1]:
                cur = stack[-1][0].right
                stack[-1][1] = False
                continue

            node,_ = stack.pop()
            res.append(node.val)

        return res