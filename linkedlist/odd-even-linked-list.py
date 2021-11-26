"""
https://leetcode.com/problems/odd-even-linked-list/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head:
            return head
        odd = None
        even = None
        o, e = odd, even
        cur = head 
        index = 0
        while cur:
            index += 1
            node = ListNode(cur.val)            
            if index % 2 == 1:
                if o:
                    o.next = node
                    o = o.next
                else:
                    odd = node
                    o = node
            else:
                if e:
                    e.next = node
                    e = e.next
                else:
                    even = node
                    e = node
            cur = cur.next
        if e:
            o.next = even
        return odd


class Solution:
    def oddEvenList(self, head):
        if not head:
            return head
        odd, even = head, head.next
        even_head = even
        while even and even.next:
        	odd.next = even.next
        	odd = odd.next
        	even.next = odd.next
        	even = even.next
        odd.next = even_head
        return head