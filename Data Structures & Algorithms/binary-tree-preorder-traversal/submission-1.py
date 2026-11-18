# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # res = []

        # def helper(root):
        #     if not root:
        #         return 
        #     res.append(root.val)
        #     helper(root.left)
        #     helper(root.right)
        # helper(root)
        # return res
        res = []

        cur = root
        stack = []

        while cur or stack:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left
            
            cur = stack.pop()
            cur = cur.right


        return res

        