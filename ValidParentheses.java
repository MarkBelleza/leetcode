class Solution {
    public boolean isValid(String s) {

        Stack<Character> stack = new Stack<Character>();

        Map<Character, Character> map = new HashMap<Character,Character>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');

        for (char chara: s.toCharArray()){
            if (map.containsKey(chara)){
                if(stack.size() == 0){
                    return false;
                }
                else if(stack.peek() != map.get(chara)){
                    return false;
                }
                stack.pop();
                
            }else{
                stack.push(chara);
            }
        }

        if (stack.size() == 0){
            return true;
        }
        return false;
    }
}

// Time: O(n)
// Space: O(n)
