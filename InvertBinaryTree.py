# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        # Time: O(n)
        # Space: O(n) / O(h) (the height of the tree)

# Why Space: O(h)
# When a recursive call is made, such as self.invertTree(root.left) or self.invertTree(root.right), the current function execution is paused.
# All local variables (like root) and the return address (where to continue after the recursive call) are stored in the call stack.

# The recursive calls to self.invertTree(root.left) and self.invertTree(root.right) don't return immediately. They "wait" until all deeper recursive calls finish.
# This "waiting" creates a stack of pending calls, which grows with the tree's height.
# Thus, the space complexity is determined by the maximum height of the tree, which represents the maximum depth of the recursion stack.
