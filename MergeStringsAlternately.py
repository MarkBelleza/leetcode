class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        
        #ans = ""
        #shortest = len(word1)

        # if len(word1) > len(word2):
        #     shortest = len(word2)

        # while shortest > 0:
        #     ans = ans + word1[0] + word2[0]
        #     word1 = word1[1:]
        #     word2 = word2[1:]
        #     shortest -= 1

        # return ans + word1 + word2
        # Time: O(n)
        # Space: O(n)

        # or
        
        ans = ""
        while word1 or word2:
            if word1:
                ans += word1[0]
                word1 = word1[1:]
            if word2:
                ans += word2[0]
                word2 = word2[1:]
        return ans
        # Time: O(n)
        # Space: O(n)
