/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        int count = 0;
        int res = 0;

        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode curr = root;

        while (count < k){
            if (curr != null){
                stack.push(curr);
                curr = curr.left;
            }
            else if (stack.size() > 0){
                curr = stack.pop();

                count++;
                res = curr.val;

                curr = curr.right;
            }
        }
        return res;
    }
    // Time: O(H + k) worst case, you'll have to travel the entire height (since its an inorder traversal, DFS) + k nodes
    // Space: O(H) worst case where H is the height of the tree
    
}
