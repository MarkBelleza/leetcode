class Solution {
    public int jump(int[] nums) {
        int jump = 0;
        int max_jump = 0;
        int curr_jump = 0;
        for (int i = 0; i < nums.length - 1; i++){
            max_jump = Math.max(max_jump, nums[i] + i);

            if (max_jump >= nums.length - 1){
                jump++;
                return jump;
            }
            if (curr_jump == i){
                jump++;
                curr_jump = max_jump;
            }
        }
        return jump;
    }
}
// Time: O(n)
// Space: O(1)
