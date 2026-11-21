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

        def dfs(node):
            if node.val in visited:
                return 
            
            new_node = Node(val=node.val)

            visited[new_node.val] = new_node

            for neg in node.neighbors:
                if neg not in visited:
                    dfs(neg)

                new_node.neighbors.append(visited[neg.val])

        dfs(node)

        return visited[1]
