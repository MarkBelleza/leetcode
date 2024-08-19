class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> s = new Stack<Integer>();

        for (String i : operations){
            if (i.equals("+")){
                s.push(s.peek() + s.get(s.size() - 2));
            }
            else if(i.equals("D")){
                s.push(s.peek() * 2);
            }
            else if(i.equals("C")){
                s.pop();
            }else{
                s.push(Integer.parseInt(i));
            }
        }

        int res = 0;
        for (int i : s){
            res += i;
        }
        return res;
    }

    // Time: O(n)
    // Space: O(n)
}
