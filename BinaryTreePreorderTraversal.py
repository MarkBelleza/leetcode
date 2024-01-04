# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Preorder:    Root -> Left -> Right 

        # Recursive solution
        # if not root:
        #     return []
        # elif not root.left and not root.right: 
        #     return [root.val]
        # elif not root.left: #if left do not exist then just go right
        #     return [root.val] + Solution.preorderTraversal(self, root.right)
        # else: return [root.val] + Solution.preorderTraversal(self, root.left) +  Solution.preorderTraversal(self, root.right)


        
        #Iterative solution
        res = []
        stack = []
        curr = root

        while True:
            if curr: #check if current node has a value
                stack.append(curr) 
                res.append(curr.val) #append since root value comes first always
                curr = curr.left #traverse the left node

            elif stack:  #if current node is empty, check stack to see if we traversed any nodes by checking the stack
                curr = stack.pop() #if true then go back to previous node 
                curr = curr.right #traverse right side after left (if right side is empty as well, the current node will traverse back again according to the stack)
            else:
                break
        return res
