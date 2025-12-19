/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode hare = head;
        ListNode turtle = head;

        while (hare != null && hare.next != null){ // no need to check if turtle is null since hare will always be ahead, thus hare will know if there is an end first
            hare = hare.next.next;
            turtle = turtle.next;

            if (turtle.equals(hare)){ //not the same as "hare.equals(turtle)" as it's possible hare is null, in which case the line fails immediately 
                return true;
            }

        }
        return false;

    }
    //Time: O(n)
    //Space: O(1)
}
