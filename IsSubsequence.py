class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        if i == len(s):
            return True
        return False
    
    # Time: O(t) the length of t, since we assume t may be longer than s in length
    # Space: O(1)
