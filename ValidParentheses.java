class Solution {
    public boolean isValid(String s) {
        
        Map<Character, Character> brackets = new HashMap<Character, Character>();
        brackets.put(')', '(');
        brackets.put('}', '{');
        brackets.put(']', '[');

        Stack<Character> stack = new Stack<Character>();

        for (char i : s.toCharArray()){
            if (!brackets.containsKey(i)){
                stack.push(i);
            }
            else if (stack.size() > 0 && stack.peek() == brackets.get(i)){
                stack.pop();
            }else{
                return false;
            }
        
        }

        if (stack.size() != 0){
            return false;
        }
        return true;
    }

    // Time: O(n)
    // Space: O(n)
}
