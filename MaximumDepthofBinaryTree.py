# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS (Breath first search) approach
        if not root: 
            return 0

        ans = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans += 1

        return ans 

    # Time: O(n) where n is the number of nodes
    # Space: O(n) worst case, the queue will hold the widest level of the tree, which would be about n/2

        # DFS(Depth First Search)
        if not root:
            return 0
        
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)

        # Time: O(n)
        # Space: O(h)


# Why Space: O(h)
# When a recursive call is made, such as self.invertTree(root.left) or self.invertTree(root.right), the current function execution is paused.
# All local variables (like root) and the return address (where to continue after the recursive call) are stored in the call stack.

# The recursive calls to self.invertTree(root.left) and self.invertTree(root.right) don't return immediately. They "wait" until all deeper recursive calls finish.
# This "waiting" creates a stack of pending calls, which grows with the tree's height.
# Thus, the space complexity is determined by the maximum height of the tree, which represents the maximum depth of the recursion stack.
