# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next       
        prev = None
        current = slow.next
        slow.next = None
        while current:
            temp = current
            current = current.next
            temp.next = prev
            prev = temp
        dummy = curr = ListNode(0)
        head1 = head
        head2 = prev
        while head1 and head2:
            if head1:
                curr.next = head1
                head1 = head1.next
                curr = curr.next
            if head2:
                curr.next = head2
                head2 = head2.next
                curr = curr.next
        curr.next = head1 or head2
