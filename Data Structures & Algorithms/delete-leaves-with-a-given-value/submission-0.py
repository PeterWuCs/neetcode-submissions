# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return True

        def dfs(node):
            if not node:
                return True

            if node.val != target and not node.left and not node.right:
                return False

            left_remove = dfs(node.left)
            right_remove = dfs(node.right)

            if left_remove:
                node.left = None
            
            if right_remove:
                node.right = None

            if node.val == target and not node.left and not node.right:
                return True


            return False

        if dfs(root):
            return None

        return root