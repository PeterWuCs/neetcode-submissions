# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1

        carry_over = False
        count = 0
        while l1 or l2 or carry_over:
            count += 1
            print(f"count{count}")
            value = 0
            if l1:
                value += l1.val
            
            if l2:
                value += l2.val
            
            if carry_over:
                value += 1
                carry_over = False
            
            if value > 9:
                carry_over = True
                l1.val = value - 10
            else:
                l1.val = value

            if not l1.next and ((l2 and l2.next) or carry_over):
                l1.next = ListNode()
        
            l1 = l1.next
            if l2:
                l2 = l2.next

        return head




