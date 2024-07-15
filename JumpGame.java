class Solution {
    public boolean canJump(int[] nums) {
        int goal = nums.length - 1;

        for (int i = goal - 1; i > -1; i--){
            if (nums[i] + i >= goal){
                goal = i;
            }
        }

        if (goal == 0){
            return true;
        }
        return false;
    }
}

// Time: O(n)
// Space: O(1)
