# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        stack1 = []

        temp = head
        count = 0
        
        while temp:
            count += 1
            temp = temp.next
        
        temp = head
        count = - ((-count)//2)
        while count:
            temp = temp.next
            count -= 1
        
        while temp:
            stack.append(temp)
            stack1.append(temp.val)
            temp = temp.next

        while stack:
            temp = head.next
            head.next = stack.pop()
            head.next.next = temp
            head = head.next.next 
        
        head.next = None
        print(stack1)


        