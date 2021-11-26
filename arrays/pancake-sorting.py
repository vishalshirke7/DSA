"""
https://leetcode.com/problems/pancake-sorting/
"""



def pancakeSort(arr):
    res = []
    for x in range(len(arr), 1, -1):
        i = arr.index(x)
        res.extend([i + 1, x])
        arr = arr[:i:-1] + arr[:i]
       	print(arr)
    return res


print('Output', pancakeSort([3, 2, 4, 1]))    