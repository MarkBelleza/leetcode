class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> map = new HashMap<Character, Integer>();

        for (char c : magazine.toCharArray()){
            if (map.containsKey(c)){
                map.put(c, map.get(c) + 1);
            }else{
                map.put(c, 1);
            }
        }

        for (char c : ransomNote.toCharArray()){
            if (map.containsKey(c) && map.get(c) > 0){
                map.put(c, map.get(c) - 1);
            }else{
                return false;
            }
        }

        return true;
    }
}

// Time: O(n + m)
// Space: O(m) m is the number of char in magazine
