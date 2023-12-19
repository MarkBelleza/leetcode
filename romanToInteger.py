class Solution:
    def romanToInt(self, s: str) -> int:
        romanNum = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        ans = 0

        for i in range(len(s)):
            if i < (len(s) - 1) and romanNum[s[i]] < romanNum[s[i + 1]]:
                ans -= romanNum[s[i]]
            else:
                ans += romanNum[s[i]]
        
        return ans
