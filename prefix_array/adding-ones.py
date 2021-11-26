"""
https://practice.geeksforgeeks.org/problems/adding-ones3628/1#
"""


class Solution:
    def update(self, a, n, updates, k):
        # Your code goes here
        for index in range(k):
            a[updates[index] - 1] += 1
        for index in range(1, n):
            a[index] += a[index - 1]