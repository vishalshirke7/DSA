"""
https://leetcode.com/problems/remove-linked-list-elements/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        while cur:
            if cur.val == val:
                if cur.next:
                    cur = cur.next
                    head = cur
                else:
                    head = None
                    cur = cur.next                    
            elif cur.next and cur.next.val == val:
                if cur.next.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None
            else:
                cur = cur.next
        return head
        