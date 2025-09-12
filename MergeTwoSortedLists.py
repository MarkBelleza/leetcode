# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ans = dummy

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                dummy.next = ListNode(list2.val, None)
                list2 = list2.next
            dummy = dummy.next
             
        if not list1:
            dummy.next = list2
        else:
            dummy.next = list1
        
        return ans.next

    #Time: O(n + m)
    #Space: O(1)
