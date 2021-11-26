"""
https://leetcode.com/problems/rotate-list/
"""


def rotateRight(head, k):
	size, cur = 0, head
	while cur:
		cur = cur.next
		size += 1
	k = k % size
	last = first = head
	for index in range(size - k):
		head = head.next
	first = head.next
	head.next = None
	temp_first = first
	while temp_first.next:
		temp_first = temp_first.next
	temp_first.next = last
	return first


	