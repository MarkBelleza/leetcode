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
        
