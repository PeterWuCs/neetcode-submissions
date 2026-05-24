# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        two = head
        while two and two.next:
            head = head.next
            two = two.next.next
            
            if head == two:
                return True


        return False
        