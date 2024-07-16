class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Let's implement the dynamic programming way using a 2D array (tabulation bottom up)
        table = [[-1 for j in range(len(s))] for i in range(len(s))]

        # Fill the diagonal of the table with 1
        for i in range(len(s)):
            table[i][i] = 1

        
        # Fill the upper side of the diagonal
        for size in range(2, len(s)+1): 
            for i in range(len(s) - size+1): 
                j = i + size-1

                if s[i] == s[j] and size == 2:
                    table[i][j] = 2
                elif s[i] == s[j]:
                    table[i][j] = table[i+1][j-1] + 2
                else:
                    table[i][j]  = max(table[i][j-1], table[i+1][j])

        return table[0][len(s)-1]

        # Time: O(n^2)
        # Space: O(n^2)
