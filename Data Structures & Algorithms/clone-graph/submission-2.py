"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        
        def dfs(n):
            if n.val in visited:
                return visited[n.val]

            n_copy = Node(n.val)
            visited[n.val] = n_copy

            for v in n.neighbors:
                n_copy.neighbors.append(dfs(v))
            return n_copy

        return dfs(node)
                

        