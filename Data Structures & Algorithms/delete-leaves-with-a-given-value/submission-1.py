# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None 

        visited = set()
        parent = {root: None}
        stack = [root]

        while stack:
            node = stack.pop()

            if not node.right and not node.left:
                if node.val == target:
                    if not parent[node]:
                        return None
                    if parent[node].left == node:
                        parent[node].left = None
                    else:
                        parent[node].right = None
            
            elif node not in visited:
                stack.append(node)
                visited.add(node)

                if node.right:
                    stack.append(node.right)
                    parent[node.right] = node
                
                if node.left:
                    stack.append(node.left)
                    parent[node.left] = node
        
        return root


            
