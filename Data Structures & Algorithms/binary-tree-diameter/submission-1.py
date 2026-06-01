# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest = 0

        def help(node):
            nonlocal largest
            if not node:
                return 0

            right = 0
            left = 0
            if node.right:
                right = 1 + help(node.right)
            
            if node.left:
                left = 1 + help(node.left)
            
            largest = max(largest, left + right)
            print(largest)
            return max(right, left)

        help(root)
        
        return largest
        


        