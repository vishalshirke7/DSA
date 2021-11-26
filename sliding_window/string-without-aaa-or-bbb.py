"""
https://leetcode.com/problems/string-without-aaa-or-bbb/
"""

#recursive
def strWithout3a3bRecur(A, B):
    if A == 0:      
        return 'b' * B
    elif B == 0:    
        return 'a' * A
    elif A == B:    
        return 'ab' * A
    elif A > B:     
        return 'aab' + strWithout3a3bRecur(A - 2, B - 1)
    else:           
        return strWithout3a3bRecur(A - 1, B - 2) + 'abb'


def strWithout3a3b(a, b):
    ans = ''
    while a + b > 0:
        if len(ans) >= 2 and ans[-1] == 'a' and ans[-2] == 'a':
            ans += 'b'
            b -= 1
        elif len(ans) >= 2 and ans[-1] == 'b' and ans[-2] == 'b':
            ans += 'a'
            a -= 1
        elif a > b:
            ans += 'a'
            a -= 1
        else:
            ans += 'b'
            b -= 1
    return ans            

# print('Output', strWithout3a3bRecur(6, 7))
print('Output', strWithout3a3b(6, 7))