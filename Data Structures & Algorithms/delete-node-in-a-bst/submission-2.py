# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def delete(node):
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            
            min_node = node.right
            last_node = node

            while min_node.left:
                last_node = min_node
                min_node = min_node.left
            

            min_node.left = node.left
            last_node.left = min_node.right
            if last_node is not node:
                min_node.right = node.right
            return min_node

        if not root:
            return root

        if root.val == key:
            return delete(root)

        node = root

        last_node = root

        while node and node.val != key:
            print(node.val)
            last_node = node
            if node.val > key:
                node = node.left
            else:
                node = node.right
        
        if not node:
            return root
        
        if node.val > last_node.val:
            last_node.right = delete(node)
        else:
            last_node.left = delete(node)

        return root


