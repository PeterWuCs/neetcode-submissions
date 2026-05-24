# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
    
        while second:
            temp = second.next

            second.next = prev
            prev = second

            second = temp

        
        first = head
        second = prev

        while second:
            temp1, temp2 = first.next, second.next
            
            second.next = temp1
            first.next = second
            

            first = temp1
            second = temp2