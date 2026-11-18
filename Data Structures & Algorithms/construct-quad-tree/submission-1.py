"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def helper(n, r, c):
            if n == 1:
                val = True if grid[r][c] else False
                return Node(val=val, isLeaf=True)
            
            n = n // 2
            topL = helper(n, r, c)
            topR = helper(n, r, c + n)
            botL = helper(n, r + n, c)
            botR = helper(n, r + n, c + n)
            
            if (topL.isLeaf and topR.isLeaf and botL.isLeaf and botR.isLeaf and 
                 topL.val == topR.val == botL.val == botR.val):
                val = True if grid[r][c] else False
                return Node(val=val, isLeaf=True)

            return Node(val=False, isLeaf=False, topLeft=topL, topRight=topR, bottomLeft=botL, bottomRight=botR)

        return helper(len(grid), 0, 0)
                
