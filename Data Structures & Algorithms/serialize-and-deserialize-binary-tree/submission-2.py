# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
                
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')

        if nodes[0] == 'N':
            return None

        root = TreeNode(val=int(nodes[0]))
        i = 1
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()

            if nodes[i] != 'N':
                leftnode = TreeNode(val=int(nodes[i]))
                node.left = leftnode
                q.append(leftnode)
            i += 1

            if nodes[i] != 'N':
                rightnode = TreeNode(val=int(nodes[i]))
                node.right = rightnode
                q.append(rightnode)
            i += 1

        return root









