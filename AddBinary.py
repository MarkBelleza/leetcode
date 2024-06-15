class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0 # 0 is same as false in boolean
        ans = ''
      
        i = len(a) - 1
        j = len(b) - 1

        while i > -1 or j > -1 or carry:
            if i > -1:
                carry += int(a[i])
                i -= 1
            if j > -1:
                carry += int(b[j])
                j -= 1
            ans = str(carry % 2) + ans #if carry = 3: concat '1', carry = 2: concat '0', carry = 1: concat '1'
            carry = int(carry/2)
        return ans

        #Time: O(max(a, b))
        #Space: O(max(a, b))
