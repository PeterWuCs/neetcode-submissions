# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        two = head
        while head and two.next:
            head = head.next
            two = two.next.next
            
            if head == two:
                return True
            if not two:
                return False

        return False
        