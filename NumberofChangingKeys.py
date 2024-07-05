class Solution:
    def countKeyChanges(self, s: str) -> int:
        last_key = s[0].lower()
        count = 0

        for char in s[1:]:
            if char.lower() != last_key:
                count += 1
                last_key = char.lower()
        
        return count

        #Time: O(n)
        #Space: O(1)
        
