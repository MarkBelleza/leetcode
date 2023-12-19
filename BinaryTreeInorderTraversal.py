# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        elif not root.left and not root.right: 
            return [root.val]
        elif not root.left: #if left do not exist then just go right
            return [root.val] + Solution.inorderTraversal(self, root.right)
        else: return Solution.inorderTraversal(self, root.left) + [root.val] + Solution.inorderTraversal(self, root.right)
