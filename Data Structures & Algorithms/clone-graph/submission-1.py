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
        print(node.val)
        visited = {}
        
        def dfs(n, copyN):

            visited[n.val] = copyN

            for i in range(len(n.neighbors)):
                if n.neighbors[i].val not in visited:
                    neighbor = Node(n.neighbors[i].val, [])
                    copyN.neighbors.append(neighbor)
                    dfs(n.neighbors[i], neighbor)
                else:
                    copyN.neighbors.append(visited[n.neighbors[i].val])



        copyNode = Node(node.val)
        dfs(node, copyNode)

        return copyNode
                

        