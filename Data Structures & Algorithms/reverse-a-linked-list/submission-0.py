# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        vals = []

        while head is not None:
            vals.append(head.val)
            head = head.next
        
        head = ListNode(vals[-1])
        temp = head
        for i in range(len(vals) - 2, -1, -1):
            temp.next = ListNode(vals[i])
            temp = temp.next
        return head