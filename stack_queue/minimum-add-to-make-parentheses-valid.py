"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""

#OWN
def minAddToMakeValid(s):
    op = 0
    close = 0
    for index in range(len(s) - 1, -1, -1):
        if s[index] == ')':
            close += 1
        else:
            if close > 0:
                close -= 1
            else:
                op += 1
    op += close
    return op        