from math import ceil, floor 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "+-*/":
                x = stack.pop()
                y = stack.pop()

                if i == "+":
                    stack.append(y + x)
                elif i == "-":
                    stack.append(y - x)
                elif i == "*":
                    stack.append(y * x)
                elif i == "/": 
                    stack.append(int(y / x)) #The division between two integers always truncates toward zero
            else:
                stack.append(int(i))

        return stack.pop()
        
        # Time: O(n)
        # Space: O(n)
