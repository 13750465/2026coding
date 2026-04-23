# week09-5.py
# Leetcode study plan 2095. Delete the Middle Node of a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = fast = slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        #print( slow.val )
        prev.next = slow.next
        return head
