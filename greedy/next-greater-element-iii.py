"""
https://www.geeksforgeeks.org/find-next-greater-number-set-digits/
https://leetcode.com/problems/next-greater-element-iii/
"""
def nextGreaterElement(n):
    """
    :type n: int
    :rtype: int
    """
    s = list(map(int, str(n)))
    i = len(s)-1
    while i-1>=0 and s[i]<=s[i-1]:
        i -= 1
        
    if i==0:
        return -1
    
    j = i
    while j+1<len(s) and s[j+1]>s[i-1]:
        j += 1
    
    s[i-1], s[j] = s[j], s[i-1]
    s[i:] = reversed(s[i:])
    ret = int(''.join(map(str, s)))
    
    return ret if ret<=((1<<31)-1) else -1


print('Output', nextGreaterElement(234157641))
# print('Output', nextGreaterElement(23456))