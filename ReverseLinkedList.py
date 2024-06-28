# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            temp = head.next
            
            head.next = prev #reverse the pointer

            prev = head #advance to the next nodes to reverse
            head = temp

        return prev
        
        #Time: O(n)
        #Space: O(1)
