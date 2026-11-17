# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left >= right:
            return head

        dummy = ListNode(val=0, next=head)
        count = 0

        cur = dummy
        while count < left - 1:
            count += 1
            cur = cur.next
        print(cur.val)
        
        def reverse(head, length):
            if not head:
                return 

            prev = head
            for _ in range(length):
                prev = prev.next
            cur = head

            while length != 0:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

                length -= 1

            return prev

        reverse_head = reverse(cur.next, right - left + 1)

        cur.next = reverse_head
        

        return dummy.next

            
            

        