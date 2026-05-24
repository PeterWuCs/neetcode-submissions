# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_dict = {}
        for i in range(len(inorder)):
            index_dict[inorder[i]] = i

        self.idx = 0
        def dfs(l,h):
            if l > h:
                return None
            
            root = TreeNode(preorder[self.idx])
            mid = index_dict[preorder[self.idx]]
            self.idx +=1
            left = dfs(l, mid-1)
            right = dfs(mid+1, h)

            root.left = left
            root.right = right

            return root



        return dfs(0, len(inorder)-1)