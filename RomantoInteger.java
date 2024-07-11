class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> num = new HashMap<Character, Integer>();
        num.put('I', 1);
        num.put('V', 5);
        num.put('X', 10);
        num.put('L', 50);
        num.put('C', 100);
        num.put('D', 500);
        num.put('M', 1000);

        int ans = 0;

        for (int i = 0; i < s.length(); i++){
            if (i < s.length() - 1 && num.get(s.charAt(i)) < num.get(s.charAt(i + 1))){
                ans = ans - num.get(s.charAt(i));
            }else{
                ans = ans + num.get(s.charAt(i));
            }
        }
        return ans;
    }
}
// Time: O(n)
// Space: O(1)
