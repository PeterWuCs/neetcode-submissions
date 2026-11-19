# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = k
        cur = root

        while cur:
            if not cur.left:
                count -= 1

                if count == 0:
                    return cur.val
                cur = cur.right
            
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                
                if prev.right:
                    prev.right = None
                    count -= 1
                    if count == 0:
                        return cur.val
                    cur = cur.right
                else:
                    prev.right = cur
                    cur = cur.left

        return -1 
