# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        hare = head

        #Tortoise and hare method, if there is a cycle in the in linked list eventually turtle and hare would point in the same node

        while hare and hare.next:
            turtle = turtle.next

            hare = hare.next #the hare moves twice as fast as the turtle
            hare = hare.next
          
            if turtle == hare:
                return True
        
        return False

        #Time: O(n)
        #Sapce: O(1)
