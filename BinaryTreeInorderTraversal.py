# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Inorder:     Left -> Root -> Right

        #Recursive solution
        # if not root:
        #     return []
        # elif not root.left and not root.right: 
        #     return [root.val]
        # elif not root.left: #if left do not exist then just go right
        #     return [root.val] + Solution.inorderTraversal(self, root.right)
        # else: return Solution.inorderTraversal(self, root.left) + [root.val] + Solution.inorderTraversal(self, root.right)


        #Iterative solution
        res = []
        stack = []
        curr = root

        while True:
            if curr: #check if current node has a value
                stack.append(curr) #store the current root node in a stack
                curr = curr.left #traverse the left node

            elif stack:  #if current node is empty, check stack to see if we traversed any nodes by checking the stack
                curr = stack.pop() #if true then go back to previous node

                res.append(curr.val) 
                curr = curr.right #traverse right side after left (if right side is empty, the current node will traverse back again)
            else:
                break
        return res

