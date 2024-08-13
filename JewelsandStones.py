class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        count = 0

        for char in stones:
            if char in j:
                count += 1
        
        return count
    
    # Time: O(n+m), n and m are the length of jewels and stones respectively
    # Space: O(n)
