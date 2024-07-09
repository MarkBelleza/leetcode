/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode((l1.val + l2.val) % 10);
        int carry = (l1.val + l2.val) / 10;

        ListNode current = head;
        l1 = l1.next;
        l2 = l2.next;

        while (l1 != null || l2 != null || carry != 0){
            if (l1 != null){
                carry = carry + l1.val;
                l1 = l1.next;
            }
            if (l2 != null){
                carry = carry + l2.val;
                l2 = l2.next;
            }

            current.next = new ListNode(carry % 10);
            current = current.next;

            carry = carry / 10;
        }
        return head;
    }
}

// Time: O(max(l1, l2))
// Space: O(max(l1, l2))
