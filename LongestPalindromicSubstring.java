class Solution {
    public String longestPalindrome(String s) {
        int maxLen = 0;
        String ans = "";

        for (int i = 0; i < s.length(); i++){
            // For odd length palindromes
            int l = i;
            int r = i;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)){ // its l >= 0, for when s.length() == 1
                int oddLen = r - l + 1;
                if (oddLen > maxLen){
                    maxLen = oddLen;
                    ans = s.substring(l, r+1);
                }
                l--;
                r++;
            }

            // For even length palindromes
            l = i;
            r = i+1;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)){
                int evenLen = r - l + 1;
                if (evenLen > maxLen){
                    maxLen = evenLen;
                    ans = s.substring(l, r+1);
                }
                l--;
                r++;
            }
        }
        return ans;
    }
    // Time: O(n^2)
    // Space: O(1)
}
