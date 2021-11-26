"""
https://www.interviewbit.com/old/problems/partition-list/
"""

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        order = list()
        cur = A
        while cur:
            if cur.val < B:
                order.append(cur.val)
            cur = cur.next
        cur = A
        while cur:
            if cur.val >= B:
                order.append(cur.val)
            cur = cur.next
        cur = A
        index = 0
        while cur:
            cur.val = order[index]
            cur = cur.next
            index += 1
        return A
        
