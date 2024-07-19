class Solution:
    def longestPalindrome(self, s: str) -> int:
        strings = set()
        ans = 0

        for char in s:
            if char in strings:
                strings.remove(char)
                ans += 2
            else:
                strings.add(char)
        
        if strings:
            ans += 1

        return ans
    
    # Time: O(n)
    # Space: O(n)
