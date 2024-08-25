# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #mine
        #if not head:
        #    return None
        #elif not head.next:
        #    return head
        
        #if head.val == head.next.val:
        #    head.next = head.next.next
        #   return self.deleteDuplicates(head)
        #else: return ListNode(head.val, self.deleteDuplicates(head.next))
        
        #or (more efficient)
         
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val: #will keep checking the next val until it is not a duplicate, then breaks the inner loop and move to the next node
                cur.next = cur.next.next
            cur = cur.next
        return head

        # Time: O(n)
        # Space: O(1) 
        
