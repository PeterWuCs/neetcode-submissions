# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def dfs(node, largest):
            if not node:
                return

            if node.val >= largest:
                res[0] += 1
            
            largest = max(largest, node.val)

            dfs(node.right, largest)
            dfs(node.left, largest)


        dfs(root, root.val)
        return res[0]