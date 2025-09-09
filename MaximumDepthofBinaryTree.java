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
    public int maxDepth(TreeNode root) {
        if (root == null){return 0;}

        Deque<TreeNode> q = new ArrayDeque<TreeNode>();
        q.add(root);
        int len = 0;

        while (q.size() > 0){
            int size = q.size();

            for(int i = 0; i < size; i++){
                TreeNode node = q.getFirst();
                q.removeFirst();

                if (node.left != null){
                    q.add(node.left);
                }
                if(node.right != null){
                    q.add(node.right);
                }
            }
            len++;
        }
        return len;
        // Time: O(n) where n is the number of nodes
        // Space: O(n) worst case, the queue will hold the widest level of the tree, which would be about n/2

        // or (DFS)

        if(root == null){
            return 0;
        }

        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
        //Time: O(n)
        //Space: O(n)
        
    }
}
