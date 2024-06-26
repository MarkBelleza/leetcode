# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0 or head.next == None:
            return head

        # Make a circle linked list, and figure out where the head would be after k rotations

        curr = head.next # keep track of prev and curr nodes
        prev = head

        # figure out the length of our LinkedList
        length = 2 # the conditions above makes sure the LinkedList is at least 2 nodes long
        while curr.next:
            length += 1
            prev = curr
            curr = curr.next

        curr.next = head # connect the linkedList so it is a looped list

        head_pos = k % length # cases for when k > length
        head_pos = length - head_pos # index position of our head
        
        for i in range(head_pos + 1): #need to include + 1 as an offset, since we start at the tail
            prev = curr
            curr = curr.next

        prev.next = None
        return curr

        #Time: O(n)
        #Space: O(1)


