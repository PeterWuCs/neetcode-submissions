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
        
        n = len(grid)

        node = Node()
        node.isLeaf = True
        node.val = True

        for i in range(1, n):
            found = False
            for j in range(1, n):
                if (grid[i][j] != grid[i][j - 1] or 
                    grid[i][j] != grid[i - 1][j] or 
                    grid[i][j] != grid[i - 1][j - 1]):
                    node.isLeaf = False
                    found = True

                    node.topLeft = self.construct([row[0 : n//2] for row in grid[0 : n//2]])
                    node.topRight = self.construct([row[n//2 : n] for row in grid[0 : n//2]])
                    node.bottomLeft = self.construct([row[0 : n//2] for row in grid[n//2 : n]])
                    node.bottomRight = self.construct([row[n//2 : n] for row in grid[n//2 : n]])
                    break
            
            if found:
                break

        node.val = False if grid[0][0] == 0 else True
        return node
                
