class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> s = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        int longest = 0;
        int len = 0;

        for (int num: nums){
            if(!s.contains(num - 1)){
                len++;

                while(s.contains(num+len)){
                    len++;
                }
                longest = Math.max(longest, len);
                len = 0;
            }
        }
        return longest;
    }
}
// Time: O(n)
// Space: O(n)
