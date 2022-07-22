# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = ListNode.next
        fast = ListNode.next.next
        while(current != fast):
            if (current == fast):
                return True
            if (current.next == null):
                return False
            
