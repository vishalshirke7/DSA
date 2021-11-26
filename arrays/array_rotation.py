"""
https://leetcode.com/problems/rotate-array/
"""
"""
Brute Force - O(n * d)

def rotate_array_brute_force(array, d):
    while d:
        temp = array[0]
        for i in range(len(array) - 1):
            array[i] = array[i + 1]
        array[len(array) - 1] = temp
        d -= 1
    print(array)
"""

"""
Using Extra Array
O(n) / O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
        nums[:] = a
"""

"""
Juggling Algorithm

def calculate_gcd(a, b):
    if a == 0:
        return b
    return calculate_gcd(b%a, a)

def rotate_array_juggline(array, d):
    array_length = len(array)
    d = d % array_length
    gcd = calculate_gcd(d, array_length)
    for i in range(gcd):
        temp = array[i]
        current_index = i
        while True:
            fast_index = current_index + d
            if fast_index >= array_length:
                fast_index = fast_index - array_length
            if fast_index == i:
                break
            array[current_index] = array[fast_index]
            current_index = fast_index
        array[current_index] = temp
    print(array)
"""

"""
Reversal Algorithm
O(n)
Reverse A to get ArB, where Ar is reverse of A.
Reverse B to get ArBr, where Br is reverse of B.
Reverse all to get (ArBr) r = BA.

def reverse_array(array, start, end):
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1        

def rotate_array_reversal(array, d):
    if d == 0:
        return
    array_length = len(array)
    d = d % array_length
    reverse_array(array, 0, d-1)
    reverse_array(array, d, array_length - 1)
    reverse_array(array, 0, array_length - 1)

array = [1, 2, 3, 4, 5]
rotate_array_reversal(array, 2)
print(array)    

"""

