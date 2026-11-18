# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        prev = None
        cur = root
        while cur and cur.val != key:
            prev = cur
            if cur.val > key:
                cur = cur.left
            else:
                cur = cur.right
        if not cur:
            return root

        def delete(root):
            
            if not root.left:
                return root.right
            
            if not root.right:
                return root.left


            cur = root.right

            while cur.left:
                cur = cur.left
            cur.left = root.left
            return root.right

        if not prev:
            return delete(root)
        
        new_node = delete(cur)

        if prev.val > key:
            prev.left = new_node
        else:
            prev.right = new_node

        return root
