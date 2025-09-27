class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = {"b" : 0,
            "a" : 0,
            "l" : 0,
            "o": 0,
            "n": 0}
 
        for i in text:
            if i in b:
                b[i] += 1

        return min(b["b"], b["a"], b["l"] // 2, b["o"] // 2, b["n"])      

        # Time: O(n)
        # Space: O(1) 
