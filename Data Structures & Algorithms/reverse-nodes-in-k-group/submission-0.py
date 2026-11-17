# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head
        
        def reverse(head, prev_p):
            cur = head
            prev = prev_p

            while cur != prev_p:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            return prev
            
        dummy = ListNode(next=head)
        reverse_head = dummy

        cur = dummy
        counter = 0

        while cur:
            cur = cur.next
            counter += 1

            if not cur:
                break 
                
            if counter == k:
                prev = cur.next

                temp = reverse_head.next

                reverse_head.next = reverse(reverse_head.next, prev)

                reverse_head = temp
                cur = prev

                counter = 1

        return dummy.next




                








