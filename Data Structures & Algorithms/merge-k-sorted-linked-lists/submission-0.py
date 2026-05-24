# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        dummy = ListNode(next=lists[0])

        for i in range(1, len(lists)):
            node = dummy
            head = dummy.next
            other = lists[i]

            while head and other:
                if head.val < other.val:
                    node.next = head
                    head = head.next
                else:
                    node.next = other
                    other = other.next
                node = node.next
                

            if not head:
                node.next = other
            if not other:
                node.next = head

        return dummy.next
        