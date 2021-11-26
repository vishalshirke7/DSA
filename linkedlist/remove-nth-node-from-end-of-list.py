"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1
        if n > size:
            return head
        count = 0
        cur = head
        while cur:
            if size - count == n:
                if cur.next:
                    head = cur.next
                else:
                    head = None
                return head
            elif (size - count) == (n + 1):
                if cur.next.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None
                return head
            cur = cur.next
            count += 1        
        return head
        