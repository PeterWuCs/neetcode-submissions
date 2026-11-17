# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        length_count = 0

        cur = head
        while cur:
            length_count += 1
            cur = cur.next
        
        breaking_point = length_count // 2 
        if length_count % 2 == 1:
            breaking_point += 1

        cur = head
        for _ in range(1, breaking_point):
            cur = cur.next
        
        second_half = cur.next
        cur.next = None

        def reverse(head):
            if not head:
                return head
            
            prev = None
            cur = head

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            return prev

        second_half = reverse(second_half)

        while head and second_half:
            temp = head.next
            head.next = second_half

            second_half = temp
            head = head.next




# 1, 2, 3, 4, 5, 6, 7




        
def print_list(head):
    to_print = ""
    cur = head
    while cur:
        to_print = to_print + str(cur.val) + ','
        cur = cur.next


    print(to_print)

