# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        hare = head

        while hare and hare.next: #no need to check if turtle is null since hare will always be ahead, thus hare will know if there is an end first
            hare = hare.next.next
            turtle = turtle.next
            if hare == turtle:
                return True
        
        return False
    
    # Time: O(N)
    # Space: O(1)
