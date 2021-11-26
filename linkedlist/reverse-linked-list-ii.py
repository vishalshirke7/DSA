"""
https://leetcode.com/problems/reverse-linked-list-ii/
"""

# OWN
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def reverse(self, numbers, l, r):
        s, e = l - 1, r - 1
        while s<e:
            numbers[s], numbers[e] = numbers[e], numbers[s]
            s += 1
            e -= 1
        return numbers
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        numbers = list()
        cur = head
        while cur:
            numbers.append(cur.val)
            cur = cur.next
        self.reverse(numbers, left, right)
        new_head = ListNode(0)
        cur = new_head
        for number in numbers:
            node = ListNode(number)
            cur.next = node
            cur = cur.next
        return new_head.next


class Solution:
    def reverseBetween(self, head, start, end):
        if not head:
            return None
        left, right = head, head
        stop = False
        def recurseAndReverse(right, start, end):
            nonlocal left, stop

            # base case. Don't proceed any further
            if end == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if start > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, start - 1, end - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers     
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next           

        recurseAndReverse(right, start, end)
        return head