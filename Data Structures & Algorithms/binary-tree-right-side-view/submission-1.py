# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = [root] if root else []
        q2 = []
        ans = []
        
        most_right = True
        while q:
            cur = q.pop(0)
            if most_right:
                ans.append(cur.val)
                most_right = False

            if cur.right:
                q2.append(cur.right)
            if cur.left:
                q2.append(cur.left)
            if not q:
                q = q2.copy()
                q2 = []
                most_right = True

        return ans