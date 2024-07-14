class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> num1 = Arrays.stream(nums1).boxed().collect(Collectors.toSet());
        Set<Integer> num2 = Arrays.stream(nums2).boxed().collect(Collectors.toSet());

        ArrayList<Integer> inter = new ArrayList<Integer>();
        for (Integer num : num1){
            if (num2.contains(num)){
                inter.add(num);
            }
        }

        // Need to convert ArrayList to primitive type int before returning
        int[] ans = new int[inter.size()];
        for (int i = 0; i < ans.length; i++){
            ans[i] = inter.get(i); //unboxing Integer to int automatically
        }

        // Or
        // int[] ans = inter.stream().mapToInt(Integer::intValue).toArray();

        return ans;
    }
}
// Time: O(n+m)
// TimeL O(n+m)
