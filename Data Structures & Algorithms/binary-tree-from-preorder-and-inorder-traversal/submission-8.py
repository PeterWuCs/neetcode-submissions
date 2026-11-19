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

        pre_order_index = 0

        def helper(low, high):
            nonlocal pre_order_index

            if low > high:
                return None
            
            root_value = preorder[pre_order_index]
            pre_order_index += 1

            root = TreeNode(val=root_value)
            index = index_dict[root_value]

            root.left = helper(low, index - 1)
            root.right = helper(index + 1, high)

            return root
            


        return helper(0, len(preorder) - 1)
