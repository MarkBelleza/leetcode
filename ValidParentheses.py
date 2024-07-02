class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        brackets = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        #Make sure the opening brackets correspond with its closing brackets
        for char in s:
            if not char in brackets:
                stack.append(char)
            elif stack and brackets[char] == stack[-1]:
                stack.pop()
            else:
                return False
        
        # #Make sure all opening brackets has a closing bracket
        if len(stack) == 0:
            return True
        else:
            return False
            
        #Time: O(n)
        #Space: O(n)
