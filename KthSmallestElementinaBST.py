# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
         #Iterative solution
        count = 0
        res = 0
        stack = []
        curr = root

        while count != k:
            if curr: #check if current node has a value
                stack.append(curr) #store the current root node in a stack
                curr = curr.left #traverse the left node

            elif stack:  #if current node is empty, check stack to see if we traversed any nodes by checking the stack
                curr = stack.pop() #if true then go back to previous node

                count += 1
                res = curr.val

                curr = curr.right #traverse right side after left (if right side is empty, the current node will traverse back again)
                
        return res

        # Time: O(n)
        # Space: O(n)
