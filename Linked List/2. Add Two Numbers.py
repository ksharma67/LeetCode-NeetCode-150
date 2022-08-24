# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l3 = ListNode(carry)
        ans = l3
        while l1 or l2:
            temp = 0
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            sum = (temp + carry)
            l3.next = ListNode(sum % 10) 
            l3 = l3.next
            carry = sum // 10 
        if carry != 0:
            l3.next = ListNode(carry)
            l3 = l3.next
        return ans.next
