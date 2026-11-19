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

        def helper(low, high, pre_root_index):
            if low > high:
                return None
            if low == high:
                return TreeNode(val=inorder[low])
            
            root_value = preorder[pre_root_index]
            root = TreeNode(val=root_value)

            index = index_dict[root_value]

            root.left = helper(low, index - 1, pre_root_index + 1)

            left_length = index - low
            root.right = helper(index + 1, high, pre_root_index + left_length + 1)


            return root
            


        return helper(0, len(preorder) - 1, 0)
