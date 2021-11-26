"""
https://leetcode.com/problems/reverse-linked-list/
"""

# 1. ITERATIVE
def reverseList(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

# 2. ITERATIVE
def reverseList(head):
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev    

# 3. RECURSION
def reverse(cur, prev=None):
    if not cur:
        return prev
    new_cur = cur.next
    cur.next = prev
    return reverse(new_cur, cur)


def reverseList(head):
    return reverse(head)


