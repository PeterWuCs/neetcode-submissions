# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        q = deque()
        p = deque()

        q.append(root)

        cur_level = []
        while q:
            node = q.popleft()
            cur_level.append(node.val)

            if node.left:
                p.append(node.left)
            if node.right:
                p.append(node.right)

            if not q:
                p, q = q, p

                res.append(cur_level)
                cur_level = []
        return res
