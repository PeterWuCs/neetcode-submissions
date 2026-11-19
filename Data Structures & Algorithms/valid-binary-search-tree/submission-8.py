# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        

        def dfs(node):
            min = node.val
            max = node.val

            if node.right:
                right_min, right_max, isBST = dfs(node.right)

                if right_min <= node.val or not isBST:
                    return (0, 0, False)
                
                max = right_max

            if node.left:
                left_min, left_max, isBST = dfs(node.left)

                if left_max >= node.val or not isBST:
                    return (0, 0, False)
                
                min = left_min
            
            return (min, max, True)
                    
            

        return dfs(root)[2]