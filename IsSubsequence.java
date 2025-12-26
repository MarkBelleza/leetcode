class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.length() > t.length()){
            return false;
        }

        int i = 0; //for s
        int j = 0; //for t

        while (i < s.length() && j < t.length()){
            if (s.charAt(i) == t.charAt(j)){
                i++;
                j++;
            }
            else{
                j++;
            }
        }

        if (i == s.length()){
            return true;
        }
        return false;
    }
}
// Time: O(t) the length of t, since we assume t may be longer than s in length
// Space: O(1)

// or

class Solution {
    public boolean isSubsequence(String s, String t) {
        int a = 0;

        for (char i: t.toCharArray()){
            if (a == s.length()){
                return true;
            }
            if (i == s.charAt(a)){
                a += 1;
            }
        }

        if (a == s.length()){
            return true;
        }
        return false;
    }
}
