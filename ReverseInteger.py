class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        ans = str(x)

        if '-' in ans:
            neg = True
            ans = ans.replace('-', '')
        
        ans = ans[::-1]
                
        if neg:
            ans = "-" + ans

        if int(ans) > 2 ** 31 - 1 or int(ans) < -2**31:
            return 0


        return int(ans)

    #Time: O(n), where n is the number of digits in the integer x
    #Space: O(1)
