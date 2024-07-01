class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num #xor, same bits = 0, not same bits = 1. the duplicates will cancel each other out.
        return ans

        #Time: O(n)
        #Space: O(1)


        # count = Counter(nums) 
        # for num, c in count.items(): 
        #     if c == 1:
        #         return num
        
        #Time: O(n)
        #Space: O(n)
