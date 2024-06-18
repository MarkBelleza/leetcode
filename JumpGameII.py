class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0 # the number of jumps needed to reach curr_index
        curr_index = 0 
        max_indedx = 0

        ''' 
        We want max_index to be the possible maximum index we could reach as we interate through the list.
        ''' 

        for i in range(len(nums) - 1): #no need to touch the last element
            max_indedx = max(max_indedx, i + nums[i])

            if max_indedx >= len(nums) - 1: #reached/passed the goal 
                jumps += 1
                break
            
            if curr_index == i:
                jumps += 1
                curr_index = max_indedx
        
        return jumps

        #Time: O(n)
        #Space: O(1)
