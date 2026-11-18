# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p:
            return False
        if not q:
            return False

        p_stack = [p]
        q_stack = [q]

        while p_stack or q_stack:
            p_node = p_stack.pop()
            q_node = q_stack.pop()

            if p_node.val != q_node.val:
                return False

            if (p_node.right and not q_node.right) or (q_node.right and not p_node.right):
                return False
            if (p_node.left and not q_node.left) or (q_node.left and not p_node.left):
                return False
            
            if p_node.right:
                p_stack.append(p_node.right)
                q_stack.append(q_node.right)

            if p_node.left:
                p_stack.append(p_node.left)
                q_stack.append(q_node.left)

        return True


            