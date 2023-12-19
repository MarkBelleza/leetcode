class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) > 1:
            stack = []
            opening = {"(" : ")", "{" : "}", "[" : "]"}
            for i in s:
                if i in opening:
                    stack.append(i)
                elif stack:
                    if (opening[stack.pop()] != i):
                        return False
                else:
                    return False
            if stack:
                return False
            return True
        else:
            return False
