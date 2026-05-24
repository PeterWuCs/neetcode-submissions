# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(q, p):
            if p and not q:
                return False
            if q and not p:
                return False
            if not q and not p:
                return True
            pq = [p]
            qq = [q]

            while pq and qq:
                nq = qq.pop(0)
                np = pq.pop(0)
                if nq.val != np.val:
                    return False
                if (nq.left and not np.left) or (not nq.left and np.left):
                    return False
                if (nq.right and not np.right) or (not nq.right and np.right):
                    return False

                if nq.left:
                    pq.append(np.left)
                    qq.append(nq.left)
                if nq.right:
                    pq.append(np.right)
                    qq.append(nq.right)
                
            return True
        
        q = [root]

        while q:
            node = q.pop(0)
            if check(node, subRoot):
                return True
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return False