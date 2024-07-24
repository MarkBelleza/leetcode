class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<Integer>();
        for (int i = 0; i < tokens.length; i++){

            if (tokens[i].equals("+")){ //Note String is an object not a primitive type, hence we need to use .equals()
                stack.push(stack.pop() + stack.pop());
            }
            else if (tokens[i].equals("-")){
                int num1 = stack.pop();
                int num2 = stack.pop();
                stack.push(num2 - num1);
            }
            else if (tokens[i].equals("*")){
                stack.push(stack.pop() * stack.pop());
            }
            else if (tokens[i].equals("/")){
                int num1 = stack.pop();
                int num2 = stack.pop();
                stack.push(num2 / num1);
            }
            else{
                stack.push(Integer.valueOf(tokens[i]));
            }
        }
        return stack.pop();
    }
}
// Time: O(n)
// Space: O(n)
