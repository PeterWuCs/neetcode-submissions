# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if not node:
                return 0
            right = 0
            left = 0

            if node.right:
                the = height(node.right)
                if the is False:
                    print("run the")
                    return False
                right = 1 + the

            if node.left:
                ll = height(node.left)
                if ll is False:
                    print("run ll")
                    return False
                left = 1 + ll

            print(right)
            print(left)

            if abs(right - left) > 1:
                return False

            return max(right, left)

        res = height(root)
        if res is False:
            return False
        return True



