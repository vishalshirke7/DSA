"""
https://leetcode.com/problems/merge-in-between-linked-lists/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        index, cur = 0, list1
        while cur:
            if index == a:
                while index != b:
                    cur = cur.next
                    index += 1
                if cur.next:
                    temp = list2
                    while temp and temp.next:
                        temp = temp.next
                    temp.next = cur.next
                    return list2
                else:
                    head  = list2
                    return head
            elif index == a - 1:
                start = cur
                while index != b:
                    start = start.next
                    index += 1
                if start.next:
                    temp = list2
                    while temp and temp.next:
                        temp = temp.next
                    temp.next = start.next
                    cur.next = list2
                    return list1
                else:
                    start.next = list2
                    return list1
            else:
                index += 1
            cur = cur.next