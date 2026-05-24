"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        temp = head

        new_head = Node(head.val)
        temp_new_head = new_head
        le_dict = {head: new_head }
        
        while head.next:
            new_head.next = Node(head.next.val)
            
            le_dict[head.next] = new_head.next

            head = head.next
            new_head = new_head.next

        new_head = temp_new_head
        while temp:
            if temp.random:
                temp_new_head.random = le_dict[temp.random]

            temp_new_head = temp_new_head.next
            temp = temp.next
            
        return new_head