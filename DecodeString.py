class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        k = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                k = (k * 10) + int(char) #to consider when k > 9 (more than 1 digits)

            elif char == '[':
                stack.append((current_str, k)) #store the current string before the '['
                
                current_str = '' #Reset variables to be used isnide the brackets
                k = 0

            elif char == ']':
                prev_str, prev_k = stack.pop()
                current_str = prev_str + (current_str * prev_k)

            else: #is character
                current_str += char

        return current_str

        #i think
        #Time: O(n) 
        #Space: O(n)
