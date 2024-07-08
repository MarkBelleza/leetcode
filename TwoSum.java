class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Brute force
        // int[] ans = new int[2];
        // for(int i = 0; i < nums.length; i++){
        //     int complement = target - nums[i];

        //     for(int j = 0; j < nums.length; j++){
        //         if ((i != j) && (nums[j] == complement)){
        //             ans[0] = i;
        //             ans[1] = j;
        //             return ans;
        //         } 
        //     }
        // }
        // return ans;

        // Time: O(n^2)
        // Space: O(1)


        // Using hashmaps
        Map<Integer, Integer> dic = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if (!dic.containsKey(complement)){
                dic.put(nums[i], i);
            } else{
                return new int[]{i, dic.get(complement)};
            }
        }
        return new int[]{}; //Return empty integer list

        // Time: O(n)
        // Space: O(1)
    }
}
