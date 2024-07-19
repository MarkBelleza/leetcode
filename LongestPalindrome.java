class Solution {
    public int longestPalindrome(String s) {
        Set<Character> strings = new HashSet<Character>();
        int ans = 0;

        for (char c: s.toCharArray()){
            if (strings.contains(c)){
                strings.remove(c);
                ans = ans + 2;
            }else{
                strings.add(c);
            }
        }

        if (strings.size() >= 1){
            ans++;
        }

        return ans;
    }
}

// Time: O(n)
// Space: O(n)
