# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, up):

            if node.val > low and node.val < up:
                r_sub = True
                l_sub = True
                if node.right:
                    r_sub = dfs(node.right, node.val, up)
                if node.left:
                    l_sub = dfs(node.left, low, node.val)

                return r_sub and l_sub
            print(node.val, low, up)
            return False

        return dfs(root, -1001, 1001)
            

        
        