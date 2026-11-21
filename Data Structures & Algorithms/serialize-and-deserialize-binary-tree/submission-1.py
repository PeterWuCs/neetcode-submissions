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

        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))

                stack.append(node.right)
                stack.append(node.left)

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        nodes = data.split(',')

        index = 0

        def dfs():
            nonlocal index
            if nodes[index] == "N":
                index += 1
                return None
            node = TreeNode(val=int(nodes[index]))

            index += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()




