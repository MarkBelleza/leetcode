class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        pld = ''

        for i in range(len(s)):
            # For odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                odd_len = r - l + 1
                if odd_len > max_len:
                    max_len = odd_len
                    pld = s[l:r+1]
                l -= 1
                r += 1

            # For even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                even_len = r - l + 1
                if even_len > max_len:
                    max_len = even_len
                    pld = s[l:r+1]
                l -= 1
                r += 1
    
        
        return pld

        # Time: O(n^2)
        # Space: O(1)
