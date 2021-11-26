"""
https://www.interviewbit.com/old/problems/maximum-absolute-difference/
"""

def maxArr(a):
    n = len(a)
    ap = [a[i] + i for i in range(n)]
    am = [a[i] - i for i in range(n)]
    return max(max(ap) - min(ap), max(am) - min(am))
