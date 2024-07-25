class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for char in magazine:
            if char in m:
                m[char] += 1
            else:
                m[char] = 1
        
        for char in ransomNote:
            if char in m and m[char] > 0:
                m[char] -= 1
            else:
                return False

        return True

    # Time: O(n + m)
    # Space: O(m) m for the number of char in magazine
