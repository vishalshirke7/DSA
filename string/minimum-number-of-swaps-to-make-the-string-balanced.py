"""
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
"""


def minSwaps(s):
    s = [char for char in s]
    balance, output, size = 0, 0, len(s)
    swap_index = size - 1
    for index in range(size):
        if s[index] == '[':
            balance += 1
        else:
            balance -= 1
        if balance == -1:
            while s[swap_index] == ']':
                swap_index -= 1
            s[swap_index], s[index] = s[index], s[swap_index]
            balance = 1
            output += 1
    return output


print('Output', minSwaps("][]["))
print('Output', minSwaps("]]][[["))
print('Output', minSwaps("[]"))